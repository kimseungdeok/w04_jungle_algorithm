# 다시 풀어봐야 한다
# 정확한 이해 필요
import sys
input = sys.stdin.readline

n = int(input())
stairs = [0] * 301
for i in range(1, n+1):
    stairs[i] = int(input())

dp = [0] * 301
dp[0] = 0
dp[1] = stairs[0]+stairs[1]
dp[2] = max(stairs[2]+stairs[0], stairs[2]+stairs[1])

for i in range(3, n+1):
    dp[i] = max(stairs[i] + dp[i-2], stairs[i] + stairs[i-1] + dp[i-3])

print(dp[n]) # n번째 값을 보겠다 == 맨 끝 인덱스 원소 값을 보겠다
