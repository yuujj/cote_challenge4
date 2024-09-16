from itertools import chain
import sys

bingo = []
n_list = []
c_bingo = [[0 for _ in range(5)] for _ in range(5)]

for _ in range(5):
    bingo.append(sys.stdin.readline().split())

for _ in range(5):
    n_list.append(input().split())
n_list = list(chain(*n_list))


def check_bingo(arr):
    cnt = 0
    # 가로
    cnt += sum([1 for line in arr if sum(line) == 5])
    # 세로
    cnt += sum([1 for line in list(zip(*arr)) if sum(line) == 5])
    # 대각선
    cnt += 1 if sum([1 for j in range(5) if arr[j][j] == 1]) == 5 else 0
    cnt += 1 if sum([1 for j in range(5) if arr[j][4-j] == 1]) == 5 else 0
    if cnt >= 3:
        return True
    else:
        return False
    
for i, n in enumerate(n_list):
    for k in range(5):
        if n in bingo[k]:
            n_idx = bingo[k].index(n)
            c_bingo[k][n_idx] = 1
            break
        else:
            continue
    
    if i >= 1:
        if check_bingo(c_bingo):
            print(i+1)
            break