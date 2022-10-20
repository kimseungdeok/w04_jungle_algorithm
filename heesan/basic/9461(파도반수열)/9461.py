import sys
input = sys.stdin.readline

dp = [0] * 101


def tri(N):
    dp[0] = 0
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1
    dp[4] = 2
    # N은 5부터
    for i in range(5, N+1):
        dp[i] = dp[i-5] + dp[i-1]
    return dp[N]


N = int(input())

for _ in range(N):
    num = int(input())
    print(tri(num))




