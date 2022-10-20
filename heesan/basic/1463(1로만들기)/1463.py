import sys
input = sys.stdin.readline

N = int(input())

dp = [0 for _ in range(N+1)] 
# N이 6이라면
# dp = [0,0,0,0,0,0,0]  i부터 1까지 가는 연산 횟수
# DP/바텀업 방식

for i in range(2, N+1):
    dp[0] = 0
    dp[1] = 0
    dp[i] = dp[i-1] + 1
    # 점화식 끝에 1을 더해주는건 연산횟수, 즉 호출횟수

    if i % 2 == 0 and dp[i] > dp[i//2] + 1:
        dp[i] = dp[i//2]+1

    if i % 3 == 0 and dp[i] > dp[i//3] + 1:
        dp[i] = dp[i//3] + 1

print(dp[N]) 
