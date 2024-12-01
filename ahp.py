import numpy as np
from typing import Union

class Abstract_AHP_Container:

    def __init__(self,base):
        '''
        base : array of dictionaries <string , float>
        '''
        self.size = len(base)
        self.depth = len(base[0].keys())
        self.container = np.zeros((self.depth,self.size,self.size))

    def comparison_matrix(self):
        raise NotImplementedError("Implement it in inheriting class")

    def extract_priorities(self):
        priority_vals = [0 for _ in range(self.depth)]
        for d in range(self.depth):
            eigenvalues, eigenvectors = np.linalg.eig(self.container[d])
            principal_eigenvector_idx = np.argmax(np.real(eigenvalues))
            principal_eigenvector = eigenvectors[:,principal_eigenvector_idx]
            principal_eigenvector /= np.sum(principal_eigenvector)
            priority_vals[d] = np.real(principal_eigenvector)
        return priority_vals


class Criterion:

    def __init__(self,criterion_name, perceived_importance : Union[float], sf = lambda x: x):
        self.name = criterion_name
        self.sf = sf
        self.priority = 0
        self.perceived_importance = perceived_importance

    def get_name(self):
        return self.name

    def get_score_func(self):
        return self.sf

    def set_priority(self,p):
        self.priority = p

class Criteria(Abstract_AHP_Container):

    def __init__(self,criteria):
        list_of_criterions = [{"perceived_importance" : crit.perceived_importance} for crit in criteria]
        super().__init__(list_of_criterions)
        self.criteria = criteria
        self.comparison_matrix()
        self.priorities = {name: val for name, val in zip([crit.name for crit in self.criteria],np.array(self.extract_priorities()).flatten())}


    def comparison_matrix(self):
        score_f = lambda x:x
        for d in range(self.depth):
            criterion_name = "perceived_importance"
            for i in range(self.size):
                for j in range(i,self.size):
                    score1 = self.criteria[i].perceived_importance
                    score2 = self.criteria[j].perceived_importance
                    self.container[d,i,j] =  score1 / score2
                    self.container[d,j,i] =  score2 / score1

    def update_criterion_priorities(self):

        for idx,(k,v) in enumerate(self.priorities.items()):
            self.criteria[idx].priority = v

class Alternatives(Abstract_AHP_Container):

    def __init__(self,alternatives,criteria):
        '''
        alternatives : array of dictionaties <string,Float>
        criterions : array of criterions

        Constraint:
        criterions size has to match the size of the dictionary keys in alternative
        criterions names ordering have to match dictionary keys ordering
        '''
        super().__init__(alternatives)
        self.criteria = criteria
        self.alternatives = alternatives
        self.comparison_matrix()
        self.priorities = {k: array for k,array in zip(self.alternatives[0].keys(),self.extract_priorities())}


    def comparison_matrix(self):
        score_f = lambda x:x
        for d in range(self.depth):
            curr_criterion = self.criteria[d]
            score_f = curr_criterion.get_score_func()
            criterion_name = curr_criterion.get_name()
            for i in range(self.size):
                for j in range(i,self.size):
                    score1 = score_f(self.alternatives[i][criterion_name])
                    score2 = score_f(self.alternatives[j][criterion_name])
                    self.container[d,i,j] =  score1 / score2
                    self.container[d,j,i] =  score2 / score1


    def set_scoring_function(f):
        self.scoring_func = f

    def get_container(self):
        return self.container


class Goal:

    class Node:
        def __init__(self):
            self.name = "generic"
            pass

        def fetch_priorities(self):
            pass


    class Alternatives_Node(Node):

        def __init__(self, alternatives: 'Alternatives'):
            if not isinstance(alternatives,Alternatives):
                raise Exception("Unsuspected object has been passed")

            super().__init__()
            self.alternatives = alternatives
            self.name = "alternatives"
            self.connected_to=[]

        def fetch_priorities(self,name):
            return self.alternatives.priorities[name]


    class Criterion_Node(Node):

        def __init__(self, criterion: 'Criterion'):
            if not isinstance(criterion,Criterion):
                raise Exception("Unsuspected object has been passed")

            super().__init__()
            self.criterion = criterion
            self.name = self.criterion.name
            self.connected_to = []
            self.isFinalCriterion = False

        def add_connection(self, node:'Node'):
            if self.isFinalCriterion and isinstance(node,self.Criterion_Node):
                print("Cannot add Criterion to Final Criterion")
                return

            if not self.connected_to and node.name == "alternatives":
                self.isFinalCriterion = True
            elif not self.isFinalCriterion and node.name == "alternatives":
                print("Cannot add Alternative to Intermediate Criterion")
                return

            self.connected_to.append(node)

        def fetch_priorities(self):
            if self.isFinalCriterion:
                total_score = self.connected_to[0].fetch_priorities(self.name)
            else:
                total_score = np.sum([node.fetch_priorities() for node in self.connected_to], axis=0)

            return self.criterion.priority * total_score

    class Goal_Node(Node):

        def __init__(self):
            super().__init__()
            self.connected_to = []
            self.name = "head"

        def add_connection(self, node:'Criterion_Node'):
            self.connected_to.append(node)

        def fetch_priorities(self):
            total_score = np.sum([node.fetch_priorities() for node in self.connected_to], axis = 0)
            return total_score


    def __init__(self,goal_name,alternatives):
        '''
        criterions : array of dictionaries
        alternatives : array of dictionaries
        '''
        self.name = goal_name
        self.alternatives = alternatives
        self.tail = self.Alternatives_Node(alternatives)
        self.head = self.Goal_Node()
        self.groups = []

    def dfs(self,start_node:'Node',search_name: 'str'):
        if start_node.name == search_name:
            return start_node

        possible = None
        for node in start_node.connected_to:
            possible = self.dfs(node,search_name)
            if possible.name == search_name:
                return possible
        return None


    def add_criterion(self, obj: Union['Criterion','Alternatives'], init_node_name : str = "head"):
        init_node = self.dfs(self.head, init_node_name)

        if isinstance(obj,Criterion):
            end_node = self.Criterion_Node(obj)
        else:
            end_node = self.Alternatives_Node(obj)

        init_node.add_connection(end_node)

    def add_alt_to_leafs_util(self,start_node):
        if not start_node.connected_to:
            start_node.add_connection(self.tail)
            return
        for node in start_node.connected_to:
            self.add_alt_to_leafs_util(node)

    def add_alt_to_leafs(self):
        self.add_alt_to_leafs_util(self.head)


    def compute_criterion_priorities(self):
        self.compute_criterion_priorities_util(self.head)

    def compute_criterion_priorities_util(self, start_node):

        list_of_criterions = [crit.criterion for crit in start_node.connected_to]
        c = Criteria(list_of_criterions)
        c.update_criterion_priorities()
        for node in start_node.connected_to:
            if not node.isFinalCriterion:
                self.compute_criterion_priorities_util(node)

    def make_decision(self):
        return self.head.fetch_priorities()

    def printTree(self):
        self.printTree_util(self.head, level=0)

    def printTree_util(self, start_node, level):
        '''
        Thank you gpt
        '''
        # Indent based on the current level to show hierarchy
        print(" " * (level * 4) + f"|-- {start_node.name}")
        for node in start_node.connected_to:
            self.printTree_util(node, level + 1)





