import math 
from typing import List, Tuple
from utils import build_final_table, check_valid_table, get_pos, table_print

def manhattan_distance(table1: List[List[int]], table2: List[List[int]]) -> int:  
    size = len(table1)
    table1_entries = [(0,0)] * (size*size)
    table2_entries = [(0,0)] * (size*size)
    for i in range(size):
        for j in range(size):
            table1_entries[table1[i][j]] = (i,j)
            table2_entries[table2[i][j]] = (i,j)
    def get_dist(idx1, idx2):
        return abs(idx1[0]-idx2[0])+abs(idx1[1]-idx2[1])
    dist = 0
    for i in range(1, size*size):
        dist += get_dist(table1_entries[i], table2_entries[i])
    return dist

def get_neighbours(table: List[List[int]]):
    zero_pos = get_pos(table, 0)
    deltas = [(-1,0), (0,-1), (1,0), (0,1)]
    dirs = ["down", "right", "up", "left"]

    def valid(pos) -> bool:
        return  0 <= pos[0] < len(table) and 0 <= pos[1] < len(table)

    swaps_dir = []
    old_pos = []
    new_pos = []
    for dir, delta in zip(dirs, deltas):
        next_idx = (zero_pos[0]+delta[0],zero_pos[1]+delta[1])
        if valid(next_idx):
            old_pos.append(zero_pos)
            new_pos.append(next_idx)
            swaps_dir.append(dir)

    return old_pos, new_pos, swaps_dir

def print_ans(path: List[str]) -> None:
    print(len(path))
    for x in path:
        print(x)
    exit(0)

def ida_star(root: List[List[int]], final_table: List[List[int]]) -> None:
    parents = []
    prev_pos = (-1,-1)
    bound = manhattan_distance(root, final_table)
    while True:
        next_dist = bounded_search(root, prev_pos, parents, 0, bound, final_table)
        bound = next_dist

def bounded_search(cur: List[List[int]], prev_pos: Tuple[int,int], parents: List[str], dist: int, bound: int, final_table: List[List[int]]) -> int:
    if cur == final_table:
        print_ans(parents)
    
    total_dist = dist + manhattan_distance(cur, final_table)
    if total_dist > bound:
        return total_dist

    min_dist = int(1e9+7)
    for (zr, zc), (nr, nc), dir in zip(*get_neighbours(cur)):
        if prev_pos == (nr, nc):
            continue  
        cur[zr][zc], cur[nr][nc] = cur[nr][nc], cur[zr][zc]
        parents.append(dir)
        min_dist = min(min_dist, bounded_search(cur, (zr, zc), parents, dist + 1, bound, final_table))
        parents.pop()
        cur[zr][zc], cur[nr][nc] = cur[nr][nc], cur[zr][zc]
    
    return min_dist

if __name__ == '__main__':
    n = int(input())
    num_rows = int(math.sqrt(n+1))

    pos = int(input())
    if pos != -1:
        pos += 1
    else:
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