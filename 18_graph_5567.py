n = int(input())
m = int(input())
array = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    array[a].append(b)
    array[b].append(a)

if len(array[1]) == 0:
    print(0)

else:
    friends = []
    for v in array[1]:
        friends += [v]
        friends += array[v]

    print(len(set(friends))-1)