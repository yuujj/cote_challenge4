from itertools import combinations

nums = [int(input()) for _ in range(9)]

combs = [comb for comb in list(combinations(nums, 7)) if sum(comb) == 100]
result = sorted(combs[0])

for n in result:
    print(n)
