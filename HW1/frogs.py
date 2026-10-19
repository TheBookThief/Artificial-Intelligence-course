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

def swap(state: str, idx1: int, idx2: int):
    state[idx1], state[idx2] = state[idx2], state[idx1]

def dfs(state: str, path: List[List[str]]):
    path.append(copy.copy(state))

    if is_final(state):
        print_path(path)

    flag = False
    count_more = 0
    count_less = 0
    idx = 0
    for i in range(len(state)):
        if state[i] == '_':
            idx = i
            flag = True
            continue 
        if state[i] == '>':
            count_more += 1
        elif state[i] == '<':
            count_less += 1
        
        if i > 1 and count_more > 0 and flag == False and state[i] == '<' and state[i-1] == '<':
            path.pop()
            return
        if i < len(state)-2 and count_less < n//2 and flag == True and state[i] == '>' and state[i+1] == '>': 
            path.pop()
            return

    if idx > 0 and state[idx-1] == '>':
        swap(state, idx, idx-1)
        dfs(state, path)
        swap(state, idx, idx-1)

    if idx > 1 and state[idx-2] == '>':
        swap(state, idx, idx-2)
        dfs(state, path)
        swap(state, idx, idx-2)

    if idx < len(state)-1 and state[idx+1] == '<':
        swap(state, idx, idx+1)
        dfs(state, path)
        swap(state, idx, idx+1)

    if idx < len(state)-2 and state[idx+2] == '<': 
        swap(state, idx, idx+2)
        dfs(state, path)
        swap(state, idx, idx+2)

    path.pop()

if __name__ == "__main__":
    n = int(input())
    initial_state = list(n*'>'+'_'+n*'<')
    final_path = []
    dfs(initial_state, final_path)
    