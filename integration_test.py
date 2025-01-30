'''
This isnt acctually an integration test lululululul
'''
from ahp import *
rooms = [{"temperature": i, "humidity": 2*i+2, "Co2": 3+2*i+i**2} for i in [1,4,9]]

print("Data on the 3 rooms (falsified):")
[print(r) for r in rooms]

c1 = Criterion("temperature",0.5, lambda x:x)
c2 = Criterion("humidity",0.5, lambda x:x)
c3 = Criterion("Co2",0.5, lambda x:x)
c4 = Criterion("RoomFeel",0.5, lambda x:x)
criterions = [c1,c2,c3]

alt = Alternatives(rooms,criterions)

print("\nHow the hirarchy looks like:")
g = Goal("Best Room",alt)
g.add_criterion(c4)
g.add_criterion(c1,"RoomFeel")
g.add_criterion(c2,"RoomFeel")
g.add_criterion(c3)
g.add_alt_to_leafs()
g.printTree()

g.compute_criterion_priorities()
decision_data = g.make_decision()
print("\nScores of all 3 rooms:", decision_data)
print("Check that 3 vals sum up to 1:", np.sum(decision_data))
