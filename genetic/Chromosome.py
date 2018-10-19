import random


class Chromosome:
    def __init__(self, knapsack_size, items):
        self.representation = []
        self.length = len(items)
        self.items = items
        self.knapsack_size = knapsack_size

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
        self.representation = new_representation[:]

    def crossover(self, other_chromosome, p_crossover):
        check = random.uniform(0, 1)
        point_crossover = random.randint(0, self.length - 1)
        first_offspring = self.representation[:]
        second_offspring = other_chromosome.representation[:]
        if check <= p_crossover:
            for i in range(point_crossover, self.length):
                first_offspring[i] = other_chromosome.representation[i]
                second_offspring[i] = self.representation[i]
        self.edit_representation(first_offspring)
        other_chromosome.edit_representation(second_offspring)

    def mutate(self, p_mutation):
        check = random.uniform(0, 1)
        for i in self.representation:
            if check <= p_mutation:
                self.flip(i)
        self.get_fitness()



    def __str__(self) -> str:
        return "".join(str(self.representation))

    def flip(self, i):
        self.representation[i] = int(not self.representation[i])

    def print_items(self):
        print(self.representation)
        for i in range(len(self.representation)):
            if self.representation[i]:
                print(self.items[i])









