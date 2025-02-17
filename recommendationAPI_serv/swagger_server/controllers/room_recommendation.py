from swagger_server.controllers.MCDA import Criterion, Alternatives, Goal
import numpy as np

def temperature_score(x,opt_small=20,opt_big=26,flexibility=4):
    if opt_small <= x <= opt_big:
        return 1
    if x < np.mean([opt_big,opt_small]):
        return np.exp(-np.power((x-opt_small),2)/(2*np.power(flexibility,2)))
    if x > np.mean([opt_big,opt_small]):
        return np.exp(-np.power((x-opt_big),2)/(2*np.power(flexibility-1,2)))

def co2_score(x,opt_small=400,opt_big=700,flexibility=100):
    if x < opt_small:
        return 1
    if x < opt_big:
        return 1 - 0.5*((x-opt_small)/(opt_big-opt_small))
    else:
        return np.max([np.exp(-np.power((x-opt_big),2)/(2*np.power(flexibility,2)))-0.5,0])
    
def humidity_score(x,opt_small=0.3,opt_big=0.5,flexibility=None):
    if x < opt_small:
        return 3.3*x
    if x < opt_big:
        return 1 
    if 1 - 3.5*(x-0.5) > 0:
        return 1 - 3.5*(x-0.5)
    return 0

def voc_score(x,opt_small=0.5,opt_big=1,flexibility=None):
    if x < opt_small:
        return 1
    if x < opt_big:
        return 1 - np.log(opt_small+x)
    return np.maximum(1/np.log(x+0.6)-1.6,0)

def light_score(x,opt_small=300,opt_big=500,flexibility=None):
    if x < opt_small:
        return np.maximum(np.exp(x/300 - 0.3)-1,0)
    if x < opt_big:
        return 1
    return np.maximum(1-0.0033*(x-500),0)

def sound_score(x,opt_small=0.35,opt_big=0.35,flexibility=None):
    if x < opt_small:
        return 1
    return np.maximum(-(1/35)*x+2,0)

CRITERIA_NAMES = ["temperature","co2_level","humidity","VOC_level","light_intensity","sound_level"]
CRITERIA_FUNCTIONS = [temperature_score, co2_score, humidity_score, voc_score, light_score, sound_score]

class RoomRecommendation:

    def __init__(self):
        self.goal = Goal("Recommend best room")

    def init_score_functions(self, optimal, flexibility):
        optimal_values = [optimal[key] for name in CRITERIA_NAMES for key in optimal if name in key]
        flexibility_values = [flexibility[key] for name in CRITERIA_NAMES for key in flexibility if name in key]
        



    
    def init_criterion(self,weights):
        self.goal.clear_criteria()
        criteria_weights = [float(weights[key]) for name in CRITERIA_NAMES for key in weights if name in key]
        self.criteria = [Criterion(name,weight,score) for name,weight,score in zip(CRITERIA_NAMES,criteria_weights,CRITERIA_FUNCTIONS)]
        for c in self.criteria:
            self.goal.add_criterion(c)

    def init_alternatives(self,alternatives):
        self.alternatives = Alternatives(alternatives,self.criteria)
        self.goal.set_alternatives(self.alternatives)
    
    def finalise(self):
        self.goal.add_alt_to_leafs()
        self.goal.compute_criterion_priorities()

    def recommend(self):
        self.result = self.goal.make_decision()
        return self.result


