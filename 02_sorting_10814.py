N = int(input())
data = list()

for n in range(N):
    age, name = map(str, input().split())
    data.append((n, int(age), name))

data = sorted(data, key=lambda x: (x[1], x[0]))

for s in data:
    print(s[1], s[2])
