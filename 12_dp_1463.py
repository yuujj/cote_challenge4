"""
메모제이션 이용
최대 -> 최소 순서 기록
(1씩 빼기 -> 2로 나눈 경우 -> 3으로 나눈 경우)
"""
n = int(input())
dp = [0] * (int(1e6)+1)

for i in range(2, n+1):
    dp[i] = dp[i-1] + 1

    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)

print(dp[n])