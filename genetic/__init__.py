from genetic.Population import Population

max_iterations = 1000
p_crossover = 0.7
p_mutation = 0.1
population_size = 200


def knapsack(knapsack_size, items):
    p = Population(population_size, knapsack_size, items)
    for i in range(max_iterations):
        p.start_selection_phase()
        p.start_crossover_phase(p_crossover)
        p.start_mutation_phase(p_mutation)
    return p.best_chromosome
