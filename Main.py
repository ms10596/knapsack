import genetic
import backtracking


def input_file():
    f = open("input.txt", "r")
    n_test_cases = int(f.readline())
    for i in range(n_test_cases):
        n_items = int(f.readline())
        print(n_items+1)
        knapsack_size = int(f.readline())
        weight_items = []
        value_items = []
        for j in range(n_items):
            line = list(map(int, f.readline().split()))
            weight_items.append(line[0])
            value_items.append(line[1])
        print("Case: " + str(i))
        # print (weight_items)
        # print (value_items)
        output(knapsack_size, n_items, weight_items, value_items)


def output(knapsack_size, n_items, weight_items, value_items):
    my_solution, best_gene = genetic.knapsack(knapsack_size, weight_items, value_items, n_items)
    # print(knapsack_size)
    # print(n_items)
    # print(weight_items)
    # print(value_items)
    optimal_solution = backtracking.knapsack(knapsack_size, weight_items, value_items, n_items)
    print("Optimal Solution: ")
    print(optimal_solution)
    print("My algorithm solution: ")
    print(my_solution)
    for i in best_gene:
        if i:
            print(weight_items[i] + " " + value_items[i])


if __name__ == '__main__':
    input_file()
