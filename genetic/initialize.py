import random
from genetic import fitness

max_population = 4


def initiate(n_items, weight_items, knapsack_size):
    decimal_population = random.sample(range(1, pow(2, n_items)), max_population)
    print(decimal_population)
    population = []
    for i in decimal_population:
        population.append(decimal_to_binary(i, n_items))
    print(population)
    return population


# def new_gene(n_items, weight_items, knapsack_size):
#     l = []
#     for i in range(n_items):
#         l.append(random.randint(0, 1))
#     if fitness.weight(l, weight_items) > knapsack_size:
#         return new_gene(n_items, weight_items, knapsack_size)
#     return l
def decimal_to_binary(x, n_items):
    binary_list = [int(x) for x in bin(x)[2:]]
    while len(binary_list) < n_items:
        binary_list.insert(0, 0)
    return binary_list


def binary_to_decimal(x):
    sum = 0
    for i in range(len(x)):
        sum += x[i] * pow(2, len(x) - 1 - i)
    return sum

