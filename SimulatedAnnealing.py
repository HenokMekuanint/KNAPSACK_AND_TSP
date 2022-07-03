from abc import ABC, abstractmethod
import math
import random


class State(ABC):

    sequence_max = 10

    def __init__(self) -> None:
        self.sequence = self.randomSequence(State.sequence_max)

    def __gt__(self, other):
        return self.getValue() > other.getValue()

    def __lt__(self, other):
        return self.getValue() < other.getValue()

    @abstractmethod
    def getValue(self):
        raise NotImplementedError("getValue must be implemented")
 
    @abstractmethod
    def randomSequence(self, max_size):
        raise NotImplementedError('randomSequence must be implemented')
    
    @abstractmethod
    def neighbors(self):
        raise NotImplementedError("neighbors must be implemented")


class SimulatedAnnealing(ABC):

    cooling_rate = 1.5
    temperature = 1000

    def __init__(self, sequence_max) -> None:
        State.sequence_max = sequence_max

    @abstractmethod
    def compare(self, firstState: State, secondState: State):
        raise NotImplementedError('compare must be implemented!')
    
    @abstractmethod
    def getRandomState(self):
        raise NotImplementedError('getRandomState must be implemented!')

    def findOptima(self):
        state = self.getRandomState()
        while True:
            if SimulatedAnnealing.temperature <= 1:
                return state
            optimum_found = False
            neighbours = state.neighbors()
            for neighbor_state in neighbours:
                if self.compare(neighbor_state, state):
                    state = neighbor_state
                    optimum_found = True
                else:
                    loss = abs(state.getValue()-neighbor_state.getValue())
                    probability = math.exp(-(loss)/SimulatedAnnealing.temperature)
                    if random.random() <= probability:
                        state = neighbor_state
                        optimum_found = True
            SimulatedAnnealing.temperature /= SimulatedAnnealing.cooling_rate
            
            if not optimum_found:
                return state








    
