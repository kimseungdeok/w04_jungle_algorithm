def fib(n, memo):

    # 어떤 경우든 기저 조건은 0과 1로 똑같고 메모이제이션에는 영향이 없다.
    if n == 0 or n == 1:
        return n

    # (memo라는) 해시 테이블을 확인해
    # fib(n)이 이미 계산됐는지 본다.
    if not memo.get(n):

        # n이 memo에 없으면 재귀로 fib(n)을 계산한 후
        # 그 결과를 해시 테이블에 저장한다.
        memo[n] = fib(n-2, memo) + fib(n-1, memo)

    # 이제 fib(n)의 결과가 확실히 memo에 들어 있다.
    # (이전부터 있었을 수도 있고 앞 코드에서 방금 저장했을 수도 있다.
    # 어쨋든 분명 들어 있다.)
    # 따라서 그 값을 반환한다.
    return memo[n]

# 빅 오는 무엇인가? N이 달라질 때 재귀 호출을 몇번하는가?
# N(원소 갯수)에 대해 (2N) - 1번 호출한다.
# O(N) 알고리즘이다.

print(fib(30, {}))
print(fib(40, {}))
print(fib(50, {}))
print(fib(60, {}))
