import random
from SimulatedAnnealing import SimulatedAnnealing, State

INFINITY = 100000000000000000

class Path(State):
    roads = {}
    cities = []
    def __init__(self) -> None:
        super().__init__()
    
    def getValue(self):
        distance = 0
        for i in range(Path.sequence_max-1):
            first_city = self.sequence[i]
            second_city = self.sequence[i+1]
            jump_distance = Path.roads.get((first_city, second_city), INFINITY)
            jump_distance = Path.roads.get((second_city, first_city), INFINITY)
            distance += jump_distance
        return distance
    
    def randomSequence(self, max_size):
        sequence = [i for i in range(max_size)]
        random.shuffle(sequence)
        return sequence
    
    def neighbors(self):
        return [Path() for _ in range(10)]


class FullPathFinder(SimulatedAnnealing):
    def __init__(self, roads: dict) -> None:
        Path.roads = roads
        city_names = set()
        for road in roads:
            city_names.add(road[0])
            city_names.add(road[1])
        Path.cities = list(city_names)
        print(city_names)
        super().__init__(len(city_names))


    def compare(self, firstState: State, secondState: State):
        return firstState < secondState

    def getRandomState(self):
        return Path()


roads = {
    ("New York", "California"): 100,
    ("New York", "Texas"): 20,
    ("New York", "Utha"): 190,
    ("Texas", "Utha"): 67,
    ("Texas", "California"): 32,
    ("Utha", "California"): 212,
}

test = FullPathFinder(roads=roads)
optima = test.findOptima()
print(optima.sequence)