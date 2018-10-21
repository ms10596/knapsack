from genetic.Population import Population


# max_iterations = 1000
# p_crossover = 0.5
# p_mutation = 0.01
# population_size = 100


def knapsack(knapsack_size, items):
    iterations = 2000
    p_crossover = 0.5
    p_mutation = 0.1
    population_size = 3
    return k(knapsack_size, items, iterations, p_crossover, p_mutation, population_size)


def k(knapsack_size, items, iterations, p_crossover, p_mutation, population_size):
    p = Population(population_size, knapsack_size, items)
    for i in range(iterations):
        p.start_refinement_phase()
        p.start_selection_phase()
        # print(p.best_chromosome)
        # print(p.second_best_chromosome)
        # print(p)
        p.start_crossover_phase(p_crossover)
        p.start_mutation_phase(p_mutation)
    return p.best_chromosome
