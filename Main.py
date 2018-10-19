import genetic
from Item import Item
from genetic.Chromosome import Chromosome

def input_file():
    f = open("input.txt", "r")
    n_test_cases = int(f.readline())
    for i in range(n_test_cases):
        n_items = int(f.readline())
        # print(n_items+1)
        knapsack_size = int(f.readline())
        items = []
        for j in range(n_items):
            line = list(map(int, f.readline().split()))
            items.append(Item(line[0], line[1]))
        print("Case: " + str(i+1))
        output(knapsack_size, items)


def output(knapsack_size, items):
    best_chromosome = genetic.knapsack(knapsack_size, items)
    # print(best_gene)
    optimal_solution = 72
    print("Optimal Solution: ")
    print(optimal_solution)
    print("My algorithm solution: ")
    print(best_chromosome.get_fitness())
    best_chromosome.print_items()


if __name__ == '__main__':
    input_file()
