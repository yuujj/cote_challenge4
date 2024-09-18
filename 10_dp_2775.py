"""
k,n가 k-1층의 n까지의 합을 갖는 리스트 생성
"""
t = int(input())
data = []

for _ in range(t):
    k = int(input())
    n = int(input())
    data.append((k, n))

    d = [[i for i in range(1, n+1)] for _ in range(k+1)]

    for i in range(1, k+1):
        for j in range(n):
            d[i][j] = sum(d[i-1][:j+1])

    print(d[k][n-1])
