import sys
input = sys.stdin.readline


# 리스트만들때 인덱스 맞춰주기 위해 0 넣고 시작하는 것 항상 주의하자.
str1 = [0] + list(input().strip())  # row
str2 = [0] + list(input().strip())  # col

dp = [[0] * len(str2) for _ in range(len(str1))]

for i in range(1, len(str1)):
    for j in range(1, len(str2)):
        if str1[i] == str2[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])

