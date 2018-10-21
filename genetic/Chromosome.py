import random


class Chromosome:
    def __init__(self, knapsack_size, items):
        random.seed(1)
        self.representation = []
        self.length = len(items)
        self.items = items
        self.knapsack_size = knapsack_size

        while len(self.representation) < self.length:
            self.representation.append(random.randint(0, 1))


    def get_fitness(self):
        total_value = 0
        # total_weight = 0
        for i in range(len(self.representation)):
            total_value += self.representation[i] * self.items[i].value
            # total_weight += self.representation[i] * self.items[i].weight
        # if total_weight > self.knapsack_size:
        #     return 0
        return total_value

    def get_weight(self):
        total_weight = 0
        for i in range(len(self.representation)):
            total_weight += self.representation[i] * self.items[i].weight
        return total_weight

    def edit_representation(self, new_representation):
        self.representation = new_representation[:]

    def crossover(self, other_chromosome, p_crossover):
        # random.seed(1)
        check = random.uniform(0, 1)
        point_crossover = random.randint(0, self.length - 1)
        if check <= p_crossover:
            self.edit_representation(
                self.representation[:point_crossover] + other_chromosome.representation[point_crossover:])
            other_chromosome.edit_representation(
                other_chromosome.representation[:point_crossover] + self.representation[point_crossover:])

    def mutate(self, p_mutation):
        # random.seed(1)
        check = random.uniform(0, 1)
        for i in self.representation:
            if check <= p_mutation:
                self.flip(i)
        self.get_fitness()

    def flip(self, i):
        self.representation[i] = int(not self.representation[i])

    def refine(self):
        if self.get_weight() > self.knapsack_size:
            for i in range(len(self.representation)):
                if self.representation[i]:
                    self.representation[i] = 0
                    # break

    def print_items(self):
        # print(self.representation)
        for i in range(len(self.representation)):
            if self.representation[i]:
                print(self.items[i])

    def __str__(self) -> str:
        return "".join(str(self.representation))
