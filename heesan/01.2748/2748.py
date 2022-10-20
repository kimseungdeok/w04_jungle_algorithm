import sys
input = sys.stdin.readline

N = int(input())

dp = [0] * 91


def fib(N):
    dp[0] = 0
    dp[1] = 1
    dp[2] = 1    
    for i in range(3,N+1):
        dp[i] = dp[i-2] + dp[i-1]
    return dp[N]



print(fib(N)) 
