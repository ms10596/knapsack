import random


class Population:
    def __init__(self, size, chromosome_length):
        self.size = size
        self.chromosome_length = chromosome_length
        self.chromosomes = []

        self.initialize_population()

    def initialize_population(self):
        while len(self.chromosomes) < self.size:
            self.chromosomes.append(self.get_random_chromosome())

    def get_random_chromosome(self):
        chromosome = []
        while len(chromosome) < self.chromosome_length:
            chromosome.append(random.randint(0, 1))
        return chromosome

    def __str__(self) -> str:
        return "hey"


if __name__ == '__main__':
    a = Population(4, 2)
    print(a)
