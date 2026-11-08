from typing import List, Tuple

def table_print(table: List[List[int]]) -> None:
    for i in range(len(table)):
        print(table[i])
    print(10*'-')

def table_to_row(table: List[List[int]]) -> List[int]:
    return [x for row in table for x in row]

def get_inversions(table: List[List[int]]) -> int:
    arr = table_to_row(table)
    arr.remove(0)
    cnt = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                cnt += 1
    return cnt

def check_valid_table_odd(table: List[List[int]], final_table: List[List[int]]) -> bool:
    cnt = get_inversions(table)
    cnt_final = get_inversions(final_table)
    return (cnt+cnt_final) % 2 == 0

def get_pos(table: List[List[int]], val: int) -> Tuple[int,int]:
    for i in range(len(table)):
        for j in range(len(table)):
            if table[i][j] == val:
                return i,j

def check_valid_table_even(table: List[List[int]], final_table: List[List[int]]) -> bool:
    cnt = get_inversions(table)
    zero_row, _ = get_pos(table, 0)
    cnt_final = get_inversions(final_table)
    zero_row_final, _ = get_pos(final_table, 0)
    return (cnt+zero_row+cnt_final+zero_row_final) % 2 == 0

def check_valid_table(table: List[List[int]], final_table: List[List[int]]) -> bool:
    if len(table) % 2 == 1:
        return check_valid_table_odd(table, final_table)
    else:
        return check_valid_table_even(table, final_table)

def build_final_table(n: int, empty_pos: int) -> List[List[int]]:
    final_table = []
    idx = 1
    for i in range(n):
        row = []
        for j in range(n):
            if i*n+j+1 == empty_pos:
                row.append(0)
            else:
                row.append(idx)
                idx += 1
        final_table.append(row)
    return final_table
