import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

dp = [1 for _ in range(n)]

# 부분 수열의 길이를 메모이제이션 하자.

for i in range(n):
    for j in range(i):  # 자신의 앞에 요소들을 보겠다.
        # 수열에서 j인덱스부터 i인덱스 까지의 부분수열의 길이를 dp에 저장한다.
        # j는 점점 i쪽으로 다가옴.

        if nums[i] > nums[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))
