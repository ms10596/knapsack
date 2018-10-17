import random
from genetic import fitness

max_population = 4


def initiate(n_items, weight_items, knapsack_size):
    population = []
    while len(population) < max_population:
        population.append(new_gene(n_items, weight_items, knapsack_size))
    return population


def new_gene(n_items, weight_items, knapsack_size):
    l = []
    for i in range(n_items):
        l.append(random.randint(0, 1))
    if fitness.weight(l, weight_items) > knapsack_size:
        return new_gene(n_items, weight_items, knapsack_size)
    return l
