from genetic.initialize import initiate
from genetic.selection import get_best_2_genes
from genetic.crossover import mate
from genetic.mutation import mutate
from genetic.fitness import fitness
from genetic.Population import Population

max_iterations = 1
population_size = 10
def knapsack(knapsack_size, items):
    p = Population(population_size, knapsack_size, items)
    p.start_selection_phase()
    p.start_crossover_phase()


    return "", ""
