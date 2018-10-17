def mate(first_gene, second_gene):
    offspring = []
    for i in range(len(first_gene)):
        if i % 2:
            offspring.append(first_gene[i])
        else:
            offspring.append(second_gene[i])
    return offspring
