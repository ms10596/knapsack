import random
def p_roulette():
    return random.randint(1, 100)
def get_best_2_genes(value_items, population):
    all_fitness = sum([fitness(gene, value_items) for gene in population])
    cumulative = []
    for i in range(len(population)):
        cumulative.append(int(fitness(population[i], value_items) / all_fitness * 100))
        if i > 0:
            cumulative[i] += cumulative[i - 1]

    first_gene = random.randint(0, 100)
    second_gene = random.randint(0, 100)
    print(cumulative)
    # print(str(first_gene) + " " + str(second_gene))
    for i in range(len(cumulative)):
        if first_gene > cumulative[i]:
            first_gene = population[i - 1]

    for i in range(len(cumulative)):
        if second_gene > cumulative[i]:
            second_gene = population[i - 1]
    return first_gene, second_gene

