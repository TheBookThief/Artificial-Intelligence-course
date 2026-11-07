import math 
from typing import List

def check_valid_table(table: List[List[int]]):
    pass

if __name__ == '__main__':
    n = int(input())
    pos = int(input())
    num_rows = int(math.sqrt(n+1))
    
    table = []
    for i in range(num_rows):
        row = [int(x) for x in input().split(' ')]
        table.append(row)
    valid = check_valid_table(table)
    print(table)