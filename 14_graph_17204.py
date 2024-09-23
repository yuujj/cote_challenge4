n, k = map(int, input().split())
nums = [int(input()) for _ in range(n)]

target, m = 0, 0

for i in range(n):
    target = nums[target]
    m += 1
    if target == k:
        print(m)
        break
else:
    print(-1)