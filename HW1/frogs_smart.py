def swap(cur: str, idx1: int, idx2: int):
    cur[idx1], cur[idx2] = cur[idx2], cur[idx1]

def single_jump(direction: int, empty_position: int, cur: str):
    if direction == 0:
        swap(cur, empty_position, empty_position-1)
        print("".join(cur))
        return empty_position-1
    else:
        swap(cur, empty_position, empty_position+1)
        print("".join(cur))
        return empty_position+1

def double_jump(direction: int, empty_position: int, cur: str) -> int:
    if direction == 0:
        swap(cur, empty_position, empty_position-2)
        print("".join(cur))
        return empty_position-2
    else:
        swap(cur, empty_position, empty_position+2)
        print("".join(cur))
        return empty_position+2

def build_sol(n: int):
    empty_position = n
    cur = list(n*'>'+'_'+n*'<')
    print("".join(cur))
    
    # get to switching pattern abab*_
    turn = 0
    for i in range(n+1):
        if i < n:
            for j in range(i):
                empty_position = double_jump(turn, empty_position, cur)
            empty_position = single_jump(turn, empty_position, cur)
        else:
            for j in range(i):
                empty_position = double_jump(turn, empty_position, cur)
        turn = 1-turn
    
    # resolve from abab*_
    for i in range(n, 0, -1):
        empty_position = single_jump(turn, empty_position, cur)
        for j in range(i-1):
            empty_position = double_jump(turn, empty_position, cur)
        turn = 1-turn

if __name__ == "__main__":
    n = int(input())
    build_sol(n)