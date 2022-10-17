import sys
input = sys.stdin.readline

N = int(input())  # 테스트 케이스 수

# 입력 값
# 동전 가짓수
# 각 동전의 금액
# 만들어야 할 금액


for _ in range(N):
    # 동전 가짓 수
    type = int(input())
    # 각각의 동전 입력 받아서 리스트에 담기
    coins = list(map(int, input().split()))
    # 목표 금액 입력
    goal = int(input())

    # memoization을 위한 리스트 선언

    # 주어진 N가지 동전으로 만들어야 할 금액 M(1 ≤ M ≤ 10000)이 주어진다.
    dp = [0] * (goal + 1)
    dp[0] = 1

    # 각 화폐 단위인 coin을 돌면서 1~goal 을 만들 수 있는지 확인한다.

    # ex ) 3
    # 1 5 10
    # 100
    for coin in coins: # coins = [1,5,10]
        # 1에 대해서
        # 0부터 100번 순회하겠다
        for i in range(goal + 1):
            
            if i >= coin:
                dp[i] += dp[i - coin]

    print(dp[goal])


