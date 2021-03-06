import random
from genetic.Chromosome import Chromosome


class Population:
    def __init__(self, size, knapsack_size, items):
        random.seed(1)
        self.size = size
        self.chromosome_length = len(items)
        self.chromosomes = []
        self.knapsack_size = knapsack_size
        self.items = items

        self.initialize_population()

        self.best_chromosome = 0
        self.second_best_chromosome = 0

    def initialize_population(self):
        while len(self.chromosomes) < self.size:
            self.chromosomes.append(Chromosome(self.knapsack_size, self.items))

    def get_all_fitness(self):
        return sum([i.get_fitness() for i in self.chromosomes])

    def get_best_chromosome(self):
        total_fitness = self.get_all_fitness()
        lucky = random.uniform(0, total_fitness)
        j = 0
        for i in self.chromosomes:
            j += i.get_fitness()
            if lucky <= j:
                return i

    def start_selection_phase(self):
        self.best_chromosome = self.get_best_chromosome()
        self.second_best_chromosome = self.get_best_chromosome()

    def start_crossover_phase(self, p_crossover):
        self.best_chromosome.crossover(self.second_best_chromosome, p_crossover)

    def start_mutation_phase(self, p_mutation):
        [i.mutate(p_mutation) for i in self.chromosomes]

    def start_refinement_phase(self):
        [i.refine() for i in self.chromosomes]


    def __str__(self) -> str:
        return "".join([str(i) for i in self.chromosomes])
