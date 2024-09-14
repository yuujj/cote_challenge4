"""
i와 i+1 비교 후 서로 변경
정렬된 상태와 같지 않다면 같아질때까지(최대5회) 반복
"""

import sys

data = list(sys.stdin.readline().split())
sorted_data = sorted(data)

def sorting(data):
	for i in range(4):
		if data[i] > data[i+1]:
			data[i], data[i+1] = data[i+1], data[i]
			print(' '.join(data))

for i in range(5):
	if sorting(data) == sorted_data:
		break
