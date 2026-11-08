import heapq
import copy
import math 
from typing import List
from utils import build_final_table, check_valid_table, get_pos, table_print

def manhattan_distance(table1: List[List[int]], table2: List[List[int]]):
    table1_entries = [(0,0)] * (len(table1)*len(table1))
    table2_entries = [(0,0)] * (len(table2)*len(table2))
    for i in range(len(table1)):
        for j in range(len(table1)):
            table1_entries[table1[i][j]] = (i,j)
            table2_entries[table2[i][j]] = (i,j)
    def get_dist(idx1, idx2):
        return abs(idx1[0]-idx2[0])+abs(idx1[1]-idx2[1])
    dist = 0
    for i in range(len(table1)*len(table1)):
        dist += get_dist(table1_entries[i], table2_entries[i])
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

    neighbours = []
    neighbours_dir = []
    for dir, delta in zip(dirs, deltas):
        next_idx = (zero_pos[0]+delta[0],zero_pos[1]+delta[1])
        if valid(next_idx):
            new_table = copy.deepcopy(table)
            # s numpy arrays polzvaneto na tuple kato index e validno, ama reshih che samo s lists moje da se opravim makar da e grozno
            new_table[zero_pos[0]][zero_pos[1]], new_table[next_idx[0]][next_idx[1]] = new_table[next_idx[0]][next_idx[1]], new_table[zero_pos[0]][zero_pos[1]] 
            neighbours.append(new_table)
            neighbours_dir.append(dir)
    return neighbours, neighbours_dir

def print_ans(path: List[List[int]]):
    print(len(path)-1)
    [print(x) for x in path[1:]]
    # print("Path is: ",path[1:])
    exit(0)

def ida_star(root: List[List[int]], final_table: List[List[int]]):
    path = [root]
    parents = [-1]
    bound = manhattan_distance(root, final_table)
    while True:
        print(20*"-")
        mini = 1e9+7
        next_dist = bounded_search(path, parents, 0, bound, final_table)
        if next_dist == -1:
            print_ans()
            break
        else:
            bound = next_dist

def bounded_search(path: List[List[int]], parents: List[List[int]], dist: int, bound: int, final_table: List[List[int]]):
    print(dist)
    table_print(path[-1])
    cur = path[-1]
    
    if cur == final_table:
        print_ans(parents)

    min_dist = 1e9+7
    for next, dir in zip(*get_neighbours(cur)):
        if next in path:
            continue
        total_dist = 1 + dist + manhattan_distance(next, final_table)
        if  total_dist <= bound:
            path.append(next)
            parents.append(dir)
            min_dist = min(min_dist, bounded_search(path, parents, dist + 1, bound, final_table))
            parents.pop()
            path.pop()
        else:
            return total_dist
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
    table_print(final_table)
    valid = check_valid_table(table, final_table)

    print(manhattan_distance(table,final_table))
    if valid == False:
        print(-1)
        exit(0)
    ida_star(table, final_table)


"""
8
-1
1 2 3
4 5 6
8 7 0
"""