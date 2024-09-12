"""
생일의 년/월을 두자리수로 채우고, 년월일을 이어진 숫자로 처리
생일 기준으로 정렬
"""
n = int(input())
data = []

for _ in range(n):
    ip = input().split()
    name, birth = ip[0], int(f"{ip[3]}{ip[2]:0>2}{ip[1]:0>2}")
    data.append([name, birth])

data = sorted(data, key=lambda x: x[1])

print(data[-1][0])
print(data[0][0])