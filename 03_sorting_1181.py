N = int(input())
data = set()

for _ in range(N):
    data.add(input())

data = sorted(data)
data = sorted(data, key=lambda x: len(x))

for s in data:
    print(s)