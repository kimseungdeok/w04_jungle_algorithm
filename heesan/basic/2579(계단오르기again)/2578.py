import sys

input = sys.stdin.readline

n = int(input())

score = [0]

for _ in range(n):
    s = int(input())
    score.append(s)

dp = [0] * (n+1)
dp[1] = score[1]
if n >= 2:
    dp[2] = score[1] + score[2]


for i in range(3, n+1):
    dp[i] = max(dp[i-3] + score[i-1] + score[i], dp[i-2] + score[i])


print(dp[n])
