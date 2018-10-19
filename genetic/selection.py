import random
from genetic.fitness import fitness


def p_roulette():
    return random.randint(1, 100)
def total_fitness(population, value_items):
    return sum([fitness(gene, value_items) for gene in population])

def get_best_2_genes(value_items, population):
    all_fitness = total_fitness(population, value_items)
    cumulative = []
    for i in range(len(population)):
        cumulative.append(fitness(population[i], value_items) / all_fitness * 100)
        if i > 0:
            cumulative[i] += cumulative[i - 1]
    first_gene =[]
    second_gene =[]
    first = random.randint(0, 100)
    second = random.randint(0, 100)
    # print(cumulative)
    # print(str(first_gene) + " " + str(second_gene))
    for i in range(len(cumulative)):
        if first > cumulative[i]:
            first_gene = population[i - 1]

    for i in range(len(cumulative)):
        if second > cumulative[i]:
            second_gene = population[i - 1]
    return first_gene, second_gene

