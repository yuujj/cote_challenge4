"""
본인보다 '큰' 사람을 찾기 -> 본인과 비교해도 상관없음
본인보다 '큰' 사람인 경우 rank+1
"""

import sys
n = int(input())
data = []

for _ in range(n):
    data.append(list(map(int, sys.stdin.readline().split())))

for i in data:
    rank = 1
    for j in data:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=' ')