from typing import List, Tuple
import random
def conflict(q1: Tuple[int,int], q2: Tuple[int,int]):
    if q1[0] == q2[0]:
        return True
    if q1[1] == q2[1]:
        return True
    if q1[0]+q1[1] == q2[0]+q2[1]:
        return True
    if abs(q1[0]-q2[0]) == abs(q1[1]-q2[1]):
        return True
    return False

def generate_random_queens(n: int):
    rows = list(range(n))
    random.shuffle(rows)
    cols = list(range(n)) 
    random.shuffle(cols)
    return list(zip(rows,cols))

def generate_greedy_queens(n: int):
    queens = []
    row_conflicts = [0] * n
    main_diag_conflicts = [0] * (2*n)
    secondary_diag_conflicts = [0] * (2*n)
    for j in range(n):
        min_conflicts = n+1
        min_rows = []
        for i in range(n):
            cur_conflicts = row_conflicts[i] + main_diag_conflicts[i+j] + secondary_diag_conflicts[i+n-j]
            if cur_conflicts < min_conflicts:
                min_conflicts = cur_conflicts
                min_rows = []
            if cur_conflicts == min_conflicts:
                min_rows.append(i)
        min_row = random.choice(min_rows)
        queens.append((min_row,j))
        row_conflicts[min_row] += 1
        main_diag_conflicts[min_row+j] += 1
        secondary_diag_conflicts[min_row+n-j] += 1 
    
    return queens

def print_matrix(n, queens: List[Tuple[int,int]]):
    print(sorted(queens))
    for q in sorted(queens):
        line = list(n * '_')
        line[q[1]] = '*'
        print()
        print(line)
                
def print_ans(n, queens: List[Tuple[int,int]]):
    print([x[1] for x in sorted(queens)])

def iterate_on_board(n, queens):
    steps = 0
    max_steps = 10 * n
    
    conflicts = [0] * n
    while steps <= max_steps:
        conflicting = []
        row_conflicts = [0] * n
        main_diag_conflicts = [0] * (2*n)
        secondary_diag_conflicts = [0] * (2*n)
        for q in queens:
            row_conflicts[q[0]] += 1
            main_diag_conflicts[q[0]+q[1]] += 1
            secondary_diag_conflicts[abs(q[0]-0)+abs(q[1]-(n-1))] += 1          

        for i in range(n):
            q = queens[i]
            if row_conflicts[q[0]] > 1:
                conflicting.append(i)
            elif main_diag_conflicts[q[0]+q[1]] > 1:
                conflicting.append(i)
            elif secondary_diag_conflicts[abs(q[0]-0) + abs(q[1]-(n-1))] > 1:
                conflicting.append(i)

        if not conflicting:
            return (True, queens)

        queen_to_change_index = random.choice(conflicting)
        queen_to_change = queens[queen_to_change_index]

        min_conflicts = n+1
        next_candidates = []
        conflicts = [0] * n

        for q in queens:
            if q == queen_to_change:
                continue
            
            #row conflict
            conflicts[q[0]] += 1
            
            #diag conflicts
            #abs(q[0]-X) = abs(q[1]-queen_to_change[1])
            if 0 <= q[0]-abs(q[1]-queen_to_change[1]) < n:
                conflicts[q[0]-abs(q[1]-queen_to_change[1])] += 1
            if 0 <= q[0]+abs(q[1]-queen_to_change[1]) < n:
                 conflicts[q[0]+abs(q[1]-queen_to_change[1])] += 1

        for i in range(n):
            if conflicts[i] < min_conflicts:
                min_conflicts = conflicts[i]
                next_candidates = []
            if conflicts[i] == min_conflicts:
                next_candidates.append(i)

        queens[queen_to_change_index] = (random.choice(next_candidates), queen_to_change[1])
        steps += 1

    return (False, queens)

def solve(n: int):
    if n < 4:
        if n == 1:
            print([0])
        else:
            print(-1)
        exit(0)

    while True:
        # queens = generate_random_queens(n) 
        queens = generate_greedy_queens(n)
        valid, queens = iterate_on_board(n, queens)
        if valid:
            break
    
    print_ans(n, queens)

if __name__ == '__main__':
    n = int(input())
    solve(n)