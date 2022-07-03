import random
import sys

from KnapSack_GA import KnapSackItem, KnapSackSolutionPopulation
from KnapSack_HC import Hill_Climbing
from KnapSack_SA import KnapSackSolution
from TravelingSalesPerson_GA import TSP_SolutionPopulation
from TravelingSalesPerson_HC import TSL
from TravelingSalesPerson_SA import FullPathFinder

  

def getRoadsFromFile(file_path: str):
    roads={}
    with open(file=file_path, mode='r') as file:
        line_number = 1
        while True:
            line_str = file.readline()
            if not line_str:
                break

            item_str = line_str
            try:
                first_city, second_city, distance = item_str.split(' ')
                roads[(first_city, second_city)] = distance
            except ValueError:
                pass            
            line_number+=1
    return roads
        

def main(algorithm: str, filePath: str):
    if algorithm == "ga":
        roads = getRoadsFromFile(file)
                
        test = TSP_SolutionPopulation(population_size=80, roads=roads)
        test.randomlyPopulate()
        test.start()
        
    elif algorithm == "hc":
        t = TSL()
        t.start("Arad")


    elif algorithm == "sa":
        roads = getRoadsFromFile(file)
        test = FullPathFinder(roads=roads)
        optima = test.findOptima()
        print(optima.sequence)


if __name__ == '__main__':
    args = sys.argv
    print(args)
    alg = args.index('--algorithm')
    file = args.index('--file')

    main(algorithm=args[alg+1], filePath=args[file+1])