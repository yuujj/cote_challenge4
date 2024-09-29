n, k = map(int, input().split())
circle = [i+1 for i in range(n)]

p = k-1
nums = []
while True:
    if len(circle) < 2:
        nums += circle
        nums = list(map(str, nums))
        text = ', '.join(nums)
        print(f"<{text}>")
        break
    nums.append(circle.pop(p))
    p = p+(k-1) if p+(k-1) < len(circle) else ((p+(k-1))%len(circle))