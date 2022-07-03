from abc import abstractmethod
import random

class Item:
    def __init__(self, weight, value, amount):
        self.weight = weight
        self.value = value
        self.amount = amount

class Hill_Climbing:
    def __init__(self):
        self.score = None
        self.current_solution = None
        self.items = self.create_items(20)
        self.maximum_weight = None
        
    def create_items(self, amount):
        items = [None for i in range(amount)]
        for i in range(amount):
            item = Item(random.randint(1, 50), random.randint(1, 50), random.randint(1, 10))
            items[i] = item
        return items
    
    def print_solutions(self, solution):
        for i in solution:
            print(i.weight, i.value, i.amount, end="")
        print()
        
    def generate_solution(self):
        total_weight = 0
        solution = []
        while True:
            item = random.choice(self.items)
            total_weight += item.weight
            if total_weight > self.maximum_weight and len(solution) != 0:
                return solution
            solution.append(item)
    
    def calculate_weight(self, solution):
        total_weight, total_value = 0, 0
        for item in solution:
            total_weight += (item.weight * item.amount)
            total_value += (item.value * item.amount)
        return (total_weight, total_value)
            
    def get_neighbours(self, solution):
        neighbours = []
        for i in range(10):
            solution = self.generate_solution()
            neighbours.append(solution.copy())
        return neighbours
    
    def get_best_neighbour(self, neighbours):
        largest_value = 0
        current_solution = None
        score = None
        for neighbour in neighbours:
            temp_score = 0
            for item in neighbour:
                temp_score += (item.value * item.amount)
            if temp_score > largest_value and temp_score < self.maximum_weight:
                current_solution = neighbour
                score = temp_score
        return (current_solution, score)
    
    def start(self, maximum_weight):
        self.maximum_weight = maximum_weight
        self.current_solution = self.generate_solution()
        _, self.score = self.calculate_weight(self.current_solution)
        while True:
            neighbours = self.get_neighbours(self.current_solution)
            solution, score = self.get_best_neighbour(neighbours)
            if solution == None:
                print()
                self.print_solutions(self.current_solution)
                print(self.score)
                break
            self.current_solution = solution
            _, self.score = self.calculate_weight(self.current_solution)
            self.print_solutions(solution)
    
    
H = Hill_Climbing()                              
H.create_items(20)
H.start(50)
