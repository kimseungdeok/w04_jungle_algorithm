"""
if a <= 0 or b <= 0 or c <= 0, then w(a, b, c) returns:
    1

if a > 20 or b > 20 or c > 20, then w(a, b, c) returns:
    w(20, 20, 20)

if a < b and b < c, then w(a, b, c) returns:
    w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)

otherwise it returns:
    w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
"""

# 재귀함수 w(a,b,c) 가 있다.
# ex) a=15,b=15,c=15 매우 오랜시간 걸림

# 이러한 재귀함수 w를 수행시간이 짧아지도록 구현하는 문제임
# 매번 값을 계산하도록 하는 형식이 아닌 한 번 계산된 값은 저장하도록 하면 된다.
# 그래서 DP 를 이용하자

# a,b,c가 주어졌을 때 , w(a,b,c) 를 출력하는 프로그램을 작성하시오
import sys
input = sys.stdin.readline


def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    if dp[a][b][c]:
        return dp[a][b][c]
    if a < b < c:
        dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1)-w(a, b-1, c)
        return dp[a][b][c]
    dp[a][b][c] = w(a-1, b, c)+w(a-1, b-1, c)+w(a-1, b, c-1)-w(a-1, b-1, c-1)
    return dp[a][b][c]


dp = [[[0] * 21 for _ in range(21)] for _ in range(21)]
# 0 ~ 20 까지 이므로


while 1:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    print(f'w({a}, {b}, {c}) = {w(a,b,c)}')
