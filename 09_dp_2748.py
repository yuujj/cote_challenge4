n = int(input())
fibo = [0, 1]

for i in range(2, 91):
    fibo.append(fibo[i-1]+fibo[i-2])

print(fibo[n])