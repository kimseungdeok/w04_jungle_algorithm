

"""
# 평범한 배낭 문제
# weight에 대해서만 관리를 해주는 걸 중점으로 보자
# why? 제한 무게를 넘는 순간 실행할 필요가 없음


4개의 물건 , 제한 무게가 7이라고 가정할 때,
            0  1  2  3  4  5  6  7
    0       0  0  0  0  0  0  0  0
A 6 / 13    0  0  0  0  0  0  13 13
B 4 / 8     0  0  0  0  8  8  13 13
C 3 / 6     0  0  0  6  8  8  13 14
D 5 / 12    0  0  0  6  8  8  13 14

이를 점화식으로 표현하면 다음과 같다.

i 번째 아이템까지 사용할 수 있을 때, j의 무게 안에서 구할 수 있는 최대 가치는

dp[i - 1][j - weight[i]] + value[i]
dp[i - 1][j]
중 더 큰 값을 가지게 된다.

가장 마지막 결과값 출력하면 됨
"""
import sys
input = sys.stdin.readline


def solve():

    n, k = map(int, input().split())

    wl = [0] # 인덱스 맞춰주기 위해서 0값을 넣고 시작한다.
    vl = [0] # 인덱스 맞춰주기 위해서 0값을 넣고 시작한다.

    for _ in range(n):
        w, v = map(int, input().split())
        wl.append(w)
        vl.append(v)

    dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

    for i in range(n+1):
        for j in range(k+1):
            if j - wl[i] >= 0:
                dp[i][j] = max(dp[i - 1][j - wl[i]] + vl[i], dp[i-1][j])
            else:
                dp[i][j] = dp[i - 1][j]

    print(dp[n][k])


solve()
