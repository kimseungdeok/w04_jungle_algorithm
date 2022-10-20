# 동전 0
# 시작 시간 :
# 끝난 시간 :

import sys
input = sys.stdin.readline


n, k = map(int, input().split())

costs = []
cnt = 0

for _ in range(n):
    cost = int(input())
    costs.append(cost)

costs.reverse()

for i in costs:
    if i > k:
        continue
    else:
        cnt = cnt + k // i
        k = k-((k//i)*i) # or (k % i)

print(cnt)


