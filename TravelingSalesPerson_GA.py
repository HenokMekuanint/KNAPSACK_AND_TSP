from heapq import heapify
import random
from GeneticAlgorithm import Chromosome, GA_Population, Gene


INFINITY = 1000000000000000000


class City(Gene):
    cities = []

    def __init__(self, bit, name) -> None:
        super().__init__(bit)
        self.name = name

    def __repr__(self) -> str:
        return self.name

    
    def flip_bit(self):
        index = random.randint(0, len(City.cities)-1)
        while index== self.bit:
            index = random.randint(0, len(City.cities)-1)

        City.cities[self.bit], City.cities[index] = City.cities[index], City.cities[self.bit]

class Path(Chromosome):

    roads = {}

    def __init__(self) -> None:
        super().__init__()

    def randomlyGenerateGenes(self):
        city_count = len(City.cities)
        sequence = [i for i in range(city_count)]
        random.shuffle(sequence)
        for i in sequence:
            self.genes.append(City(bit=i, name=City.cities[i]))
    
    def fitness(self) -> float:
        distance = 0
        city_count = len(City.cities)
        for i in range(city_count-1):
            first_city = self.genes[i].name
            second_city = self.genes[i+1].name
            road_distance = Path.roads.get((first_city,second_city), INFINITY)
            road_distance = Path.roads.get((second_city, first_city), INFINITY) if road_distance==INFINITY else road_distance
            distance += road_distance
        return distance
            


class TSP_SolutionPopulation(GA_Population):

    def __init__(self, population_size, roads: dict) -> None:
        super().__init__(population_size)
        Path.roads = roads
        cities = set()
        for i in roads.keys():
            cities.add(i[0])
            cities.add(i[1])

        City.cities = list(cities)
    
    def getAcceptedAverageFitness(self):
        pass

    def crossOver(self, father_chromosome: Chromosome, mother_chromosome: Chromosome) -> Chromosome:
        offsprint_1 = Path()
        offsprint_1.genes = father_chromosome.genes[:Chromosome.gene_count//2]+mother_chromosome.genes[Chromosome.gene_count//2:]
        offsprint_2 = Path()
        offsprint_2.genes = father_chromosome.genes[Chromosome.gene_count//2:]+mother_chromosome.genes[:Chromosome.gene_count//2]
        
        return (offsprint_1, offsprint_2)

    def randomlyPopulate(self):
        for _ in range(self.population_size):
            new_chrom = Path()
            new_chrom.randomlyGenerateGenes()
            self.individuals.append(new_chrom)
        heapify(self.individuals)

    
roads =  {
    ('New York', 'California'): 20,
    ('New York', 'texas'): 100,
    ('New York', 'nevada'): 50,
    ('California', 'utah'): 99,
    ('California', 'nevada'): 200,
    ('California', 'texas'): 10
}

test = TSP_SolutionPopulation(population_size=80, roads=roads)

test.randomlyPopulate()
test.start()
print(test.individuals)
print(len(test.individuals))
print(test.fittest())
print(len(test.individuals))



    
