from genetic.initialize import initiate
from genetic.selection import get_best_2_genes
from genetic.crossover import mate
from genetic.mutation import mutate

max_iterations = 5
def knapsack(knapsack_size, weight_items, value_items, n_items):
    for i in range(max_iterations):
        population = initiate(n_items, weight_items, knapsack_size)
        first_gene, second_gene = get_best_2_genes(value_items, population)
        first_offspring, second_offspring = mate(first_gene, second_gene)
        first_offspring, second_offspring = mutate(first_offspring, second_offspring)
        population.append(first_offspring)
        population.append(second_offspring)
    print(population)
    return "", ""