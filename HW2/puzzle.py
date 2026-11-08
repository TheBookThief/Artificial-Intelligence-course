import heapq
import copy
import math 
from typing import List, Tuple
from utils import build_final_table, check_valid_table, get_pos, table_print

def hash_table(table):
    base = 57
    MOD = int(1e9+7)
    hash = 0
    for x in table:
        for y in x:
            hash *= base
            hash += y
            hash %= MOD
    return hash
        
def manhattan_distance(table1: List[List[int]], table2: List[List[int]], cache_dist):
    hash = hash_table(table1)
    if hash in cache_dist:
        return cache_dist[hash]  
    table1_entries = [(0,0)] * (len(table1)*len(table1))
    table2_entries = [(0,0)] * (len(table2)*len(table2))
    for i in range(len(table1)):
        for j in range(len(table1)):
            table1_entries[table1[i][j]] = (i,j)
            table2_entries[table2[i][j]] = (i,j)
    def get_dist(idx1, idx2):
        return abs(idx1[0]-idx2[0])+abs(idx1[1]-idx2[1])
    dist = 0
    for i in range(1, len(table1)*len(table1)):
        dist += get_dist(table1_entries[i], table2_entries[i])
    cache_dist[hash] = dist 
    return dist

def get_neighbours(table: List[List[int]]):
    zero_pos = get_pos(table, 0)
    deltas = [(-1,0), (0,-1), (1,0), (0,1)]
    dirs = ["down", "right", "up", "left"]

    def valid(pos):
        if pos[0] < 0 or pos[0] >= len(table):
            return False
        if pos[1] < 0 or pos[1] >= len(table):
            return False
        return True

    swaps = []
    swaps_dir = []
    for dir, delta in zip(dirs, deltas):
        next_idx = (zero_pos[0]+delta[0],zero_pos[1]+delta[1])
        if valid(next_idx):
            swaps.append(zero_pos+next_idx)
            swaps_dir.append(dir)

    return swaps, swaps_dir

def print_ans(path: List[List[int]]):
    print(len(path)-1)
    [print(x) for x in path[1:]]
    exit(0)

def ida_star(root: List[List[int]], final_table: List[List[int]]):
    parents = [-1]
    cache_dist = {}
    prev_pos = (-1,-1)
    bound = manhattan_distance(root, final_table, cache_dist)
    while True:
        mini = int(1e9+7)
        next_dist = bounded_search(root, prev_pos, parents, 0, bound, final_table, cache_dist)
        if next_dist == -1:
            print_ans()
            break
        else:
            bound = next_dist

def bounded_search(cur: List[List[int]], prev_pos: Tuple[int,int], parents: List[str], dist: int, bound: int, final_table: List[List[int]], cache_dist):
    if cur == final_table:
        print_ans(parents)
    
    total_dist = dist + manhattan_distance(cur, final_table, cache_dist)
    if total_dist > bound:
        return total_dist

    min_dist = int(1e9+7)
    for ind, dir in zip(*get_neighbours(cur)):
        if prev_pos[0] == ind[2] and prev_pos[1] == ind[3]:
            continue  
        cur[ind[0]][ind[1]], cur[ind[2]][ind[3]] = cur[ind[2]][ind[3]], cur[ind[0]][ind[1]]
        parents.append(dir)
        min_dist = min(min_dist, bounded_search(cur, (ind[0], ind[1]), parents, dist + 1, bound, final_table, cache_dist))
        parents.pop()
        cur[ind[0]][ind[1]], cur[ind[2]][ind[3]] = cur[ind[2]][ind[3]], cur[ind[0]][ind[1]]
    
    return min_dist

if __name__ == '__main__':
    n = int(input())
    num_rows = int(math.sqrt(n+1))

    pos = int(input())
    if pos != -1:
        pos += 1
    if pos == -1:
        pos = num_rows*num_rows
    
    table = []
    for i in range(num_rows):
        row = [int(x) for x in input().split(' ')]
        table.append(row)

    final_table = build_final_table(num_rows, pos)
    valid = check_valid_table(table, final_table)
    if valid == False:
        print(-1)
    else:
        ida_star(table, final_table)