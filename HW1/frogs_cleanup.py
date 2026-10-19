# Cleaned version:
# changed is_final to be more pythonic with all()
# fixed type annotation
# cleanup moving logic to use predefined states
# I think these are unnecessary to spend time on right now but I acknowledge them:
# 1) I can stop copying the strings and save pairs of swaps
# 2) Tracking the '_' with O(1) is possible but anyway I have to check for invalid state in O(n)
# 3) I can decouple the logic for finding an invalid state and for tracking the '_' smartly

import copy

def print_path(path: list[list[str]]) -> None:
    print("\n".join(["".join(p) for p in path]))
    exit(0)

def is_final(state: list[str]) -> bool:
    return (
        state[n] == '_'
        and all(e == '<' for e in state[:n])
        and all(e == '>' for e in state[n+1:])
    )

def swap(state: str, idx1: int, idx2: int) -> None:
    state[idx1], state[idx2] = state[idx2], state[idx1]

def dfs(state: str, path: list[list[str]], n) -> None:
    path.append(copy.copy(state))

    if is_final(state):
        print_path(path)

    seen_empty = False
    left_frogs = 0
    right_frogs = 0
    idx = 0
    for i, cell in enumerate(state):
        if cell == '_':
            idx = i
            seen_empty = True
            continue 
        if cell == '>':
            left_frogs += 1
        elif cell == '<':
            right_frogs += 1
        
        if i > 1 and left_frogs > 0 and seen_empty == False and cell == '<' and state[i-1] == '<':
            path.pop()
            return
        if i < len(state)-2 and right_frogs < n//2 and seen_empty == True and cell == '>' and state[i+1] == '>': 
            path.pop()
            return

    MOVES = [
        (-1, '>'),
        (-2, '>'),
        (1 , '<'),
        (2 , '<')
    ]
    for delta, frog_type in MOVES:
        source_idx = idx + delta
        if 0 <= source_idx < len(state) and state[source_idx] == frog_type:
            swap(state, idx, source_idx)
            dfs(state, path, n)
            swap(state, idx, source_idx)

    path.pop()

if __name__ == "__main__":
    n = int(input())
    initial_state = list(n*'>'+'_'+n*'<')
    final_path = []
    dfs(initial_state, final_path, n)
    