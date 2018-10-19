import random


class Chromosome:
    def __init__(self, knapsack_size, items):
        self.representation = []
        self.length = len(items)
        self.items_value = items
        self.knapsack_size = knapsack_size
        self.p_crossover = 0.5

        while len(self.representation) < self.length:
            self.representation.append(random.randint(0, 1))

    def get_fitness(self):
        total_value = 0
        total_weight = 0
        for i in range(len(self.representation)):
            total_value += self.representation[i] * self.items[i].value
            total_weight += self.representation[i] * self.items[i].weight
        if total_weight > self.knapsack_size:
            return 0
        return total_value

    def edit_representation(self, new_representation):
        self.representation = new_representation

    def crossover(self, other_chromosome):
        p_crossover = random.uniform(0, 1)
        point_crossover = random.randint(0, self.length - 1)
        first_offspring = self.representation[:]
        second_offspring = other_chromosome.representation[:]
        if p_crossover <= self.p_crossover:
            for i in range(point_crossover, self.length):
                first_offspring[i] = other_chromosome.representation[i]
                second_offspring[i] = self.representation[i]
        self.edit_representation(first_offspring)
        other_chromosome.edit_representation(second_offspring)


    def __str__(self) -> str:
        return "".join(str(self.representation))










