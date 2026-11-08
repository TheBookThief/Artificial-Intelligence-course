from typing import List

def table_print(table: List[List[int]]):
    for i in range(len(table)):
        print(table[i])
    print(10*'-')

def table_to_row(table: List[List[int]]):
    return [x for row in table for x in row]

def get_inversions(table: List[List[int]]):
    arr = table_to_row(table)
    arr.remove(0)
    cnt = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                cnt += 1
    return cnt

def check_valid_table_odd(table: List[List[int]], final_table: List[List[int]]):
    cnt = get_inversions(table)
    cnt_final = get_inversions(final_table)
    if (cnt+cnt_final) % 2 == 0:
        return True
    else:
        return False

def get_pos(table: List[List[int]], val: int):
    for i in range(len(table)):
        for j in range(len(table)):
            if table[i][j] == val:
                return i,j

def check_valid_table_even(table: List[List[int]], final_table: List[List[int]]):
    cnt = get_inversions(table)
    zero_row, _ = get_pos(table, 0)
    cnt_final = get_inversions(final_table)
    zero_row_final, _ = get_pos(table, 0)
    
    if (cnt+zero_row+cnt_final+zero_row_final) % 2 == 0:
        return True
    else:
        return False

def check_valid_table(table: List[List[int]], final_table: List[List[int]]):
    if len(table) % 2 == 1:
        return check_valid_table_odd(table, final_table)
    else:
        return check_valid_table_even(table, final_table)

def build_final_table(n: int, empty_pos: int):
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
