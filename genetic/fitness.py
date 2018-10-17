def fitness(gene, value_items):
    total_fitness = 0
    for i in gene:
        total_fitness += gene[i] * value_items[i]
    return total_fitness


def weight(gene, weight_items):
    total_weight = 0
    for i in gene:
        total_weight += gene[i] * weight_items[i]
    return total_weight
