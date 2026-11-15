from typing import List, Tuple
import math
import random
def generate_initial_population(n: int, population_size: int):
    population = []
    for i in range(population_size):
        population.append([random.randint(0,1) for i in range(n)])
    return population

def fitness(arr: List[int], n: int, items: List[Tuple[int,int]], m: int):
    weight = 0
    cost = 0
    for i in range(n):
        if arr[i] == 1:
            weight += items[i][0]
            cost += items[i][1]
            if weight > m:
                return -math.inf
    return cost

def generate_parents(population_size: int, population: List[List[int]], population_fitness: List[int]):
    parents_indices = [] 
    for i in range(population_size):
        idx1, idx2 = random.randint(0, population_size-1), random.randint(0, population_size-1)
        if population_fitness[idx1] < population_fitness[idx2]:
            idx1, idx2 = idx2, idx1
        
        coinflip = random.random()
        #67 to 33 to choose the better one for a parent
        if coinflip <= 0.67:
            parents_indices.append(idx1)
        else:
            parents_indices.append(idx2)
    return parents_indices


def solve(m, n, items):
    POPULATION_SIZE = 500
    population = generate_initial_population(n, POPULATION_SIZE)
    # print(len(population), len(population[0]))
    while True:
        population_fitness = [fitness(x, n, items, m) for x in population]
        population_parents = generate_parents(POPULATION_SIZE, population, population_fitness)
        # population_crossover = crossover_population(POPULATION_SIZE, population_parents)

if __name__ == '__main__':
    m, n = [int(x) for x in input().split(" ")]
    items = []
    for i in range(n):
        wi, ci = [int(x) for x in input().split(" ")]
        items.append((wi,ci))
    solve(m, n, items)