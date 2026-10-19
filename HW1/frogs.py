from typing import List
import copy

def print_path(path: List[List[str]]):
    print("\n".join(["".join(p) for p in path]))
    # for i in range(len(path)):
    #     print("".join(path[i]))
    exit(0)

def is_final(state: List[str]) -> bool:
    for i in range(len(state)//2):
        if state[i] != '<':
            return False
    for i in range(len(state)//2+1, len(state)):
        if state[i] != '>':
            return False
    return True

def swap(state, idx1, idx2):
    state[idx1], state[idx2] = state[idx2], state[idx1]

def dfs(state: str, path: List[List[str]]):
    path.append(copy.copy(state))

    if is_final(state):
        print_path(path)

    for i in range(len(state)):
        if state[i] != '_': 
            continue
        if i > 0 and state[i-1] == '>':
            swap(state, i, i-1)
            dfs(state, path)
            swap(state, i, i-1)

        if i > 1 and state[i-2] == '>':
            swap(state, i, i-2)
            dfs(state, path)
            swap(state, i, i-2)

        if i < len(state)-1 and state[i+1] == '<':
            swap(state, i, i+1)
            dfs(state, path)
            swap(state, i, i+1)

        if i < len(state)-2 and state[i+2] == '<': 
            swap(state, i, i+2)
            dfs(state, path)
            swap(state, i, i+2)

    path.pop()

if __name__ == "__main__":
    n = int(input())
    initial_state = list(n*'>'+'_'+n*'<')
    final_path = []
    dfs(initial_state, final_path)
    