# Cleaned version: 
# - Merged the 2 jump functions in one
# - Fixed type annotations
# I think these are unnecessary but I acknowledge them:
# 1) save only the pairs of swaps instead of full strings
# 2) group the printing at the end

def swap(state: str, idx1: int, idx2: int) -> None:
    state[idx1], state[idx2] = state[idx2], state[idx1]

def jump(direction: int, empty_position: int, state: list[str], step_size: int) -> int:
    swap(state, empty_position, empty_position + direction * step_size)
    print("".join(state))
    return empty_position + direction * step_size

def build_sol(n: int) -> None:
    empty_position = n
    state = list(n*'>'+'_'+n*'<')
    print("".join(state))
    
    # get to switching pattern abab*_
    direction = -1
    for i in range(n+1):
        for _ in range(i):
            empty_position = jump(direction, empty_position, state, 2)
        if i < n:
            empty_position = jump(direction, empty_position, state, 1)
        direction *= -1
    
    # resolve from abab*_
    for i in range(n, 0, -1):
        empty_position = jump(direction, empty_position, state, 1)
        for _ in range(i-1):
            empty_position = jump(direction, empty_position, state, 2)
        direction *= -1

if __name__ == "__main__":
    n = int(input())
    build_sol(n)