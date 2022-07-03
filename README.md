Assignment II
Make a group of a maximum of 3 students (30 pts)
1. The knapsack problem is a problem in combinatorial optimization: Given a set of items,
each with a weight and a value, determine the number of each item included in a
collection so that the total weight is less than or equal to a given limit and the total value
is as large as possible.
Write three algorithms (Genetic Algorithm, Hill Climbing, and Simulated Annealing) to
solve the knapsack problem. Your algorithm should take a file on the command line in
the following fashion:
python knapsack.py --algorithm ga --file my-file.txt
The input file should have content in the following style
50
item,weight,value
phone,0.19,1000
Laptop,1.1,700
The first line in the content is the maximum weight in kilograms that your knapsack can
handle. The second line is the headers of the succeeding lines and your algorithm
should ignore it. The third and onwards should have a comma-separated list of an item’s
name, its weight in kilogram, and the item's value in USD. The list should contain 10, 15,
and 20 items. It might be tiresome to write 20 items, hence, write some randomized
program that generates such a list for you.
2. The traveling salesperson problem (TSP) (30 pts)
Write three algorithms (Genetic Algorithm, Hill Climbing, and Simulated Annealing) to
solve the TSP problem. Your algorithm should take a file on the command line in the
following fashion:
python tsp.py --algorithm ga --file my-file.txt
The input file should contain the Romania city list that you used in Assignment I.
Your deliverables should be the code for each question and a report. The report should have a
brief explanation of the benchmark of the speed of your algorithms compared to each other and
their performance compared with each other. In the first question case, compare your algorithms
in 10, 15, and 20 list cases. In question 2 case, compare your algorithms based on 8, 16, and
20 cities cases. Finally, briefly discuss what you observed. You can use a table or a graph to
present your findings.
