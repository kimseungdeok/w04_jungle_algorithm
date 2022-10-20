# 재귀 호출에 비해 동적 프로그래밍이 얼마나 빠른지 확인해 보자.

import sys
sys.stdin.readline

n = int(input())

# count = 0

def fib(n):
    # global count
    # 함수 실행 횟수는 return 실행횟수의 2배하고 -1 한만큼이다.
    # count += 1

    # 실행횟수가 곧 값인가?
    # 왜 그런가 생각해보면 결국 값을 얻을 수 있는 건 n == 1. n == 2일 때 뿐,
    # return 1이 되고 1+1+1+1+1+1~ 이런식으로 값을 더하는 것이기 떄문에
    # 피보나치 수열의 n번쨰 값이 곧
    if n == 1 or n == 2:
        return 1  # 코드1
    else:
        return (fib(n - 1) + fib(n - 2))

    # fib(4) 가 return이 3번실행
    # fib(5) 가 return이 5번실행


def fibonacci_dynamic(n):
    # fibo_memo란 memoization을 위한 정적으로 선언한 배열, 사용시 초기화 필요
    dp = [0] * (n+1)
    # dp = [0,1,1,2,0,0,0,0,0,0,0,0,0,0,0,0,~~~]
    # 실행횟수들이 각 인덱스에 저장
    dp[1], dp[2] = 1, 1
    cnt = 0
    for i in range(3, n+1):
        cnt += 1
        dp[i] = dp[i - 1] + dp[i - 2]  # 코드2
    return cnt


print(fib(n), fibonacci_dynamic(n))
# print(count)
