import random
import sys

from KnapSack_GA import KnapSackItem, KnapSackSolutionPopulation
from KnapSack_HC import Hill_Climbing
from KnapSack_SA import KnapSackSolution


def randomName():
    name = ''
    rand_chars = [random.randint(97, 122) for _ in range(8)]
    print(rand_chars)
    for i in rand_chars:
        name += chr(i)
    return name

def randomlyGenerateItems(count: int):
    with open('items_'+str(count)+'.txt', mode='w') as file:  
        max_weight = random.randint(100, 1000)
        file.write(str(max_weight)+'\n')
        file.write('item,weight,value \n')
        
        for _ in range(count):
            name = randomName()
            value = random.randint(0, 1000)
            weight = random.randint(0, 200)
            file.write(name+','+str(weight)+','+str(value)+'\n')     

def getItemsFromFile(file_path: str):
    items = []
    max_weight = None
    with open(file=file_path, mode='r') as file:
        line_number = 1
        while True:
            line_str = file.readline()
            if not line_str:
                break
            if line_number == 1:
                max_weight_str = line_str[:-1]
                max_weight = float(max_weight_str)
            elif line_number > 2:
                item_str = line_str
                try:
                    name_str, weight_str, value_str = item_str.split(',')
                    print(name_str, weight_str, value_str)
                except ValueError:
                    pass

                items.append(KnapSackItem(name_str, 0, float(value_str[:-1]), float(weight_str)))
            line_number+=1
    return (items, max_weight)
        

def main(algorithm: str, filePath: str):
    # randomlyGenerateItems(count=10)
    # randomlyGenerateItems(count=15)
    # randomlyGenerateItems(count=20)
    if algorithm == "ga":
        items, max_weight = getItemsFromFile(file_path=filePath)   
                     
        knapsack_solutions = KnapSackSolutionPopulation(population_size=80, max_total_weight=max_weight, items=items)
        knapsack_solutions.randomlyPopulate()
        knapsack_solutions.start()
        print(knapsack_solutions.fittest())
        
    elif algorithm == "hc":
        H = Hill_Climbing()                              
        H.create_items(20)
        H.start(50)


    elif algorithm == "sa":

        items, max_weight = getItemsFromFile(file_path=filePath)
        print(len(items))
        test = KnapSackSolution(items=items, max_weight=max_weight)
        optima = test.findOptima()
        print(optima.sequence)


if __name__ == '__main__':
    args = sys.argv
    print(args)
    alg = args.index('--algorithm')
    file = args.index('--file')

    main(algorithm=args[alg+1], filePath=args[file+1])