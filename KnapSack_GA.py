from heapq import heapify
import random
from GeneticAlgorithm import Chromosome, GA_Population, Gene


class KnapSackItem(Gene):
    def __init__(self, name, bit, value, weight) -> None:
        super().__init__(bit)
        self.name = name
        self.value = value
        self.weight = weight

    def flip_bit(self):
        self.bit = random.randint(0, 3)

    def __repr__(self) -> str:
        return self.name+": "+str(self.bit)+" -- "+str(self.value)+" -- "+str(self.weight)

class KnapSack(Chromosome):
    max_total_weight = 1000
    items = []

    def __init__(self) -> None:
        super().__init__()
    
    def randomlyGenerateGenes(self):
        for i in range(KnapSack.gene_count):
            bit = random.randint(0, 3)
            value = KnapSack.items[i].value
            weight = KnapSack.items[i].weight
            name = KnapSack.items[i].name

            self.genes.append(KnapSackItem(name=name, bit=bit, value=value, weight=weight))
    
    def fitness(self) -> float:
        knapsack_weight = sum([item.bit*item.weight for item in self.genes])
        if knapsack_weight <= KnapSack.max_total_weight:
            return sum([item.bit*item.value for item in self.genes])
        return 0.0


class KnapSackSolutionPopulation(GA_Population):
    
    def __init__(self, population_size, max_total_weight, items: list) -> None:
        super().__init__(population_size)
        KnapSack.gene_count = len(items)
        KnapSack.max_total_weight = max_total_weight
        KnapSack.items = items
    
    def getAcceptedAverageFitness(self):
        return KnapSack.max_total_weight

    def crossOver(self, father_chromosome: Chromosome, mother_chromosome: Chromosome) -> Chromosome:
        offsprint_1 = KnapSack()
        offsprint_1.genes = father_chromosome.genes[:Chromosome.gene_count//2]+mother_chromosome.genes[Chromosome.gene_count//2:]
        offsprint_2 = KnapSack()
        offsprint_2.genes = father_chromosome.genes[Chromosome.gene_count//2:]+mother_chromosome.genes[:Chromosome.gene_count//2]
        
        return (offsprint_1, offsprint_2)

    def randomlyPopulate(self):
        for _ in range(self.population_size):
            new_chrom = KnapSack()
            new_chrom.randomlyGenerateGenes()
            self.individuals.append(new_chrom)
        heapify(self.individuals)


items = [
    KnapSackItem('abc', 0, value=100, weight=52),
    KnapSackItem('efg', 0, value=120, weight=12),
    KnapSackItem('hij', 0, value=50, weight=123),
]


test = KnapSackSolutionPopulation(population_size=80, max_total_weight=123, items=items)
test.randomlyPopulate()
test.start()
print(test.individuals)
print(len(test.individuals))
print(test.fittest())
print(len(test.individuals))
