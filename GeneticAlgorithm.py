from heapq import heappop
import heapq
import random
from abc import ABC, abstractmethod



class Gene(ABC):
    def __init__(self, bit) -> None:
        self.bit =  bit

    @abstractmethod
    def flip_bit(self):
        raise NotImplementedError("Must override repr")

    @abstractmethod
    def __repr__(self) -> str:
        raise NotImplementedError("Must override repr")


class Chromosome(ABC):
    gene_count = 10

    def __init__(self) -> None:
        self.genes = []
        self.mutation_rate = 0.05

        self.punishment = 0
    
    def __repr__(self) -> str:
        return str(self.genes)
    
    def __lt__(self, other):
        return -self.fitness() < -other.fitness()

    @abstractmethod
    def randomlyGenerateGenes(self):
        raise NotImplementedError("Must override randomlyGenereGenes")
        
    def __iter__(self):
        for gene in self.genes:
            yield gene

    def mutate(self) -> None:
        for gene in self.genes:
            comp = random.uniform(0.0, 1.0)
            if comp < self.mutation_rate:
                gene.flip_bit()

    @abstractmethod
    def fitness(self) -> float:
        raise NotImplementedError("Must override fitness")


class GA_Population(ABC):

    def __init__(self, population_size) -> None:
        self.individuals = []
        self.population_size = population_size
        self.generation = 0

    @abstractmethod
    def randomlyPopulate(self):
        raise NotImplementedError("Must override randomlypopulate")

    def selectParents(self) -> tuple:
        father = heappop(self.individuals)
        mother = heappop(self.individuals)        
        return (father, mother)

    @abstractmethod
    def crossOver(self, father_chromosome: Chromosome, mother_chromosome: Chromosome) -> Chromosome:
        raise NotImplementedError("Must override crossover")

    def fittest(self)->Chromosome:
        return heapq.nsmallest(1, self.individuals)[0]

    def newGeneration(self):
        offsprings = []
        while len(offsprings) < self.population_size//2:
            father, mother = self.selectParents()
            offspring_1, offspring_2 = self.crossOver(father_chromosome=father, mother_chromosome=mother)
            offspring_1.mutate()
            offspring_2.mutate()
            offsprings.append(offspring_1)
            offsprings.append(offspring_2)
        self.individuals = offsprings
        self.generation += 1
    
    def averageFitness(self):
        return sum([chrom.fitness() for chrom in self.individuals])/len(self.individuals)
    
    @abstractmethod
    def getAcceptedAverageFitness(self):
        raise NotImplementedError("Must override randomlypopulate")

    def start(self):
        print("start")
        while True:
            self.newGeneration()
            print(self.averageFitness(), "==============================>")
            if self.averageFitness() > 0:
                break




