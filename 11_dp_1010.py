"""
m과 n의 조합 구현
"""
t = int(input())

def factorial(x):
    if x == 0 or x == 1:
        return 1
    return factorial(x-1)*x


for _ in range(t):
    n, m = map(int, input().split())
    bridge = factorial(m) // (factorial(n)*factorial(m-n))
    print(bridge)
