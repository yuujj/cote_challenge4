n = int(input())
pn = [0] * (n+1)

for i in range(1, n+1):
    if i == 1 or i == 2:
        pn[i] = 1
    else: pn[i] = pn[i-1] + pn[i-2]
    
print(pn[n])