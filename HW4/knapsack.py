from typing import List, Tuple
import copy
import math
import random
def generate_initial_population(n: int, population_size: int):
    population = []
    for i in range(population_size):
        population.append([])
        for j in range(n):
            if random.randint(1, 100) <= 99:
                population[i].append(0)
            else:
                population[i].append(1)
        # population.append([random.randint(0,1) for _ in range(n)])
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

def crossover_population(population_size: int, n: int, population: List[List[int]], population_parents: List[int]):
    #signle point crossover
    crossover_population = []
    for i in range(0, population_size, 2):
        p1_idx, p2_idx = population_parents[i], population_parents[i+1]
        crossover_prob = random.random()
        #60 to 40 to crossover
        if crossover_prob <= 0.6:
            crossover_idx = random.randint(1,n-1)
            c1 = copy.deepcopy(population[p1_idx][:crossover_idx]) + copy.deepcopy(population[p2_idx][crossover_idx:])
            c2 = copy.deepcopy(population[p2_idx][:crossover_idx]) + copy.deepcopy(population[p1_idx][crossover_idx:])   
            crossover_population.append(c1)
            crossover_population.append(c2)
        else:
            c1 = copy.deepcopy(population[p1_idx])
            c2 = copy.deepcopy(population[p2_idx])
            crossover_population.append(c1)
            crossover_population.append(c2)
    return crossover_population

def mutate_population(population_size: int, n: int, population: List[List[int]]):
    for i in range(population_size):
        for j in range(n):
            if random.randint(0,n-1) == 0:
                population[i][j] = 1-population[i][j]
    return population

def solve(m, n, items):
    POPULATION_SIZE = 500
    population = generate_initial_population(n, POPULATION_SIZE)
    # print(len(population), len(population[0]))
    population_last = 0
    population_last_count = 0
    while population_last_count < 10:
        population_fitness = [fitness(x, n, items, m) for x in population]
        # print(population, population_fitness)
        # print("Iteration max fitness: ", max(population_fitness))
        print(max(population_fitness))
        population_parents = generate_parents(POPULATION_SIZE, population, population_fitness)
        # print(population_parents)
        population_crossover = crossover_population(POPULATION_SIZE, n, population, population_parents)
        # print(population_crossover)
        population_mutated = mutate_population(POPULATION_SIZE, n, population_crossover)
        # print(population_mutated)
        population = population_mutated
        if max(population_fitness) == population_last:
            population_last_count += 1
        else:
            population_last = max(population_fitness)
            population_last_count = 1

if __name__ == '__main__':
    m, n = [int(x) for x in input().split(" ")]
    items = []
    for i in range(n):
        wi, ci = [int(x) for x in input().split(" ")]
        items.append((wi,ci))
    solve(m, n, items)




"""
5000 5
90 150
130 35
1530 200
500 160
150 60
"""