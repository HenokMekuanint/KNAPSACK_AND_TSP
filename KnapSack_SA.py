import random
from SimulatedAnnealing import SimulatedAnnealing, State


class KnapSackItem:
    def __init__(self, name, value, weight) -> None:
        self.name = name
        self.value = value
        self.weight = weight

    def __repr__(self) -> str:
        return self.name + " -- "+str(self.value)+","+str(self.weight)

class KnapSack(State):
    items = []
    max_weight = None

    def __init__(self) -> None:
        super().__init__()
    
    def neighbors(self):
        return [KnapSack() for _ in range(10)]
    
    def randomSequence(self, max_size):
        sequence = [i for i in range(max_size+1)]
        random.shuffle(sequence)
        return sequence[:max_size]

    def getValue(self):
        print(self.items)
        print(self.sequence)
        value = sum([self.sequence[i]*self.items[i].value for i in range(len(KnapSack.items))])
        weight = sum([self.sequence[i]*self.items[i].weight for i in range(len(KnapSack.items))])
        if weight <= KnapSack.max_weight:
            return value
        else:
            return 0.0

class KnapSackSolution(SimulatedAnnealing):

    def __init__(self, items, max_weight) -> None:
        super().__init__(len(items))
        KnapSack.items = items
        KnapSack.max_weight = max_weight
    
    def compare(self, firstState: State, secondState: State):
        return firstState > secondState

    def getRandomState(self):
        return KnapSack()


items = [
    KnapSackItem(name='Phone', value=100, weight=32),
    KnapSackItem(name='Tv', value=200, weight=234),
    KnapSackItem(name='Laptop', value=300, weight=67),
    
]


test = KnapSackSolution(items=items, max_weight=234)
optima = test.findOptima()
print(optima.sequence)