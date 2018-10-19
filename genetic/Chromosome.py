import random


class Chromosome:
    def __init__(self, items_value, knapsack_size):
        self.representation = []
        self.length = len(items_value)
        self.items_value = items_value
        self.knapsack_size = knapsack_size

        while len(self.representation) < self.length:
            self.representation.append(random.randint(0, 1))

    def get_fitness(self):
        total = 0
        for i in range(len(self.representation)):
            total += self.representation[i] * self.items_value[i]
        if total > self.knapsack_size:
            return 0
        return total

    def edit_representation(self, new_representation):
        self.representation = new_representation

    def __str__(self) -> str:
        return str(self.representation)


if __name__ == '__main__':
    x = Chromosome([1, 2, 3], 5)
    print(x)
    print(x.get_fitness())
    x.edit_representation([0, 1])
    print(x)