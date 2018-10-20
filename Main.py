from genetic import knapsack
from Item import Item
from numpy import *
import matplotlib.pyplot as plt


def inputs():
    my_answers = []
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
        my_answers.append(knapsack(knapsack_size, items))
    return my_answers


def answers():
    f = open("output.txt", "r")
    return list(map(int, f.read().split()))


if __name__ == '__main__':
    right_answers = answers()
    chromosomes = inputs()
    my_answers = [i.get_fitness() for i in chromosomes]
    my_range = range(0, 20)
    plt.xticks(my_range)
    plt.plot(my_answers, 'r')
    plt.plot(right_answers, 'g')
    plt.show()
    j = 0
    for i in chromosomes:
        j += 1
        print("Case", j, ":", i.get_fitness())
        i.print_items()
