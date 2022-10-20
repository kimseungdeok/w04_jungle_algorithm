import sys
input = sys.stdin.readline

# 자연수 받기
N = int(input())

# 범위 설정
dp = [0] * 1000001


def tile(N):
    dp[0] = 0
    dp[1] = 1
    dp[2] = 2

    for i in range(3, N+1):  # i가 7부터 시작 함
        dp[i] = (dp[i-2] + dp[i-1]) % 15746
        # 리스트에 담을 때 담는 횟수는 똑같지만 큰수를 계속 담으면 메모리를 계속 먹는다.
        # 사칙연산에 대해선 시간이 많이 걸리진 않는다.
        # 문제에서 15746 < hint

    return dp[N]


print(tile(N))
