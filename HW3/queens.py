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

def is_sol(n: int, queens: List[Tuple[int,int]]):
    for i in range(len(queens)):
        for j in range(i+1, len(queens)):
            q1 = queens[i]
            q2 = queens[j]
            if conflict(q1, q2):
                return False
    return True

def generate_random_queens(n: int):
    rows = list(range(n))
    random.shuffle(rows)
    cols = list(range(n)) 
    random.shuffle(cols)
    return list(zip(rows,cols))

def print_ans(queens: List[Tuple[int,int]]):
    print([x[1] for x in sorted(queens)])

def iterate_on_board(n, queens):
    steps = 0
    max_steps = 10*n
    while steps <= max_steps:
        conflicting = []
        for i in range(len(queens)):
            for j in range(len(queens)):
                if i == j: 
                    continue
                if conflict(queens[i], queens[j]):
                    conflicting.append(i)
                    break

        if not conflicting:
            return queens

        queen_to_change_index = random.choice(conflicting)
        queen_to_change = queens[queen_to_change_index]

        min_conflicts = n+1
        next_candidates = []
        for i in range(n):
            candidate_q = (i,queen_to_change[1]) 
            candidate_conflicts = 0
            for q in queens:
                if conflict(q, candidate_q):
                    candidate_conflicts += 1
            # it always conflicts with its old position, doesn't matter codewise, but it's cleaner ideawise
            candidate_conflicts -= 1
            if candidate_conflicts < min_conflicts:
                next_candidates = []
                min_conflicts = candidate_conflicts

            if candidate_conflicts == min_conflicts:
                next_candidates.append(candidate_q)

        queens[queen_to_change_index] = random.choice(next_candidates)
        steps += 1

    return queens

def solve(n: int):
    if n < 4:
        print(-1)
        exit(0)
    queens = generate_random_queens(n)
    while not is_sol(n, queens):
        queens = generate_random_queens(n) 
        queens = iterate_on_board(n, queens)
    print_ans(queens)

if __name__ == '__main__':
    n = int(input())
    solve(n)