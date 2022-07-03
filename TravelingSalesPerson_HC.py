
import random
from graph import graph

class TSL:
    def __init__(self):

        self.graph = g = graph()
        self.score = None
        self.current_solution = None
        self.start_node = None
        g.load_graph("graph.txt")

    def generate_solution(self):
        solution = random.sample(list(t.graph.nodes.keys()), 20)
        solution.remove(self.start_node)
        solution.insert(0, self.start_node)
        solution.append(self.start_node)
        return solution

    def has_connection(self, start, end):
        for _, i in self.graph.nodes[start].edges:
            if i ==  end:
                return True
        return False

    def calculate_weight(self, solution):
        total_weight = 0
        for i in range(len(solution) - 1):
            current_node = solution[i]
            neighbour = solution[i+1]
            if self.has_connection(current_node,neighbour):
                total_weight +=  self.graph.edges[(current_node, neighbour)].weight
            else:
                total_weight += 100
        return total_weight

    def get_neighbours(self, solution):
        neighbours = []
        for i in range(10):
            solution = self.generate_solution()
            neighbours.append(solution.copy())
        return neighbours
    
    def get_best_neighbour(self, neighbours):
        current_solution = None
        score = self.score
        for neighbour in neighbours:
            temp_score = self.calculate_weight(neighbour)
            if temp_score < score:
                current_solution = neighbour
                score = temp_score
        return (current_solution, score)

    def start(self, start_node):
        self.start_node = start_node
        self.current_solution = self.generate_solution()
        self.score = self.calculate_weight(self.current_solution)
        while True:
            neighbours = self.get_neighbours(self.current_solution)
            solution, score = self.get_best_neighbour(neighbours)
            if solution == None:
                print(self.current_solution)
                print(self.score)
                break
            self.current_solution = solution
            self.score = self.calculate_weight(self.current_solution)

            
t = TSL()
# print(t.calculate_weight(t.generate_solution()))
# print(t.has_connection("Arad", "Zerind"))
t.start("Arad")

