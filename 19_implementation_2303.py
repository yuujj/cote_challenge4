from itertools import combinations

n = int(input())
data = []

for _ in range(n):
    data.append(list(map(int, input().split())))

combo = [max([str(sum(nums))[-1] for nums in list(combinations(d, 3))]) for d in data]
combo_list = [(i+1, v) for i, v in enumerate(combo)]

print(sorted(combo_list, reverse=True, key=lambda x: (x[1], x[0]))[0][0])
