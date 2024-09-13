"""
점수를 배열로 받고 내림차순 정렬한 후, k번째 점수를 출력
"""

n, k = map(int, input().split())
scores = list(map(int, input().split()))

print(sorted(scores, reverse=True)[k-1])