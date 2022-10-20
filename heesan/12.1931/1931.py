import sys
from time import time
input = sys.stdin.readline

n = int(input())

time_table = []

for _ in range(n):
    c = list(map(int, input().split()))
    time_table.append(c)

# 가능한 가장 많은 회의의 수를 알기 위해서는 '빨리 끝내는 회의 순서대로 정렬을 해야 한다.'
# 빨리 끝낼수록 뒤에서 고려해볼 회의가 많기 때문이다.
# 빨리 시작하는 순서대로 정렬을 우선 한다면, 오히려 늦게 끝날 수 있기 때문이다.
# 한 가지 더 고려 해야함.
# 만약 끝나는 시간이 같을 경우에 빨리 시작하는 순서로 정렬되어야 가능한 더 많이 할 수 있는 회의의 경우의 수가 많아진다.

# 그렇기 때문에
# 1. 끝나는 시간의 오름차순
# 2. 시작하는 시간의 오름차순
# 이 두 가지를 고려 해주어야 한다.

time_table.sort(key=lambda x: (x[1], x[0]))


cnt = 1
end_time = time_table[0][1]

for i in range(1,n):
    if time_table[i][0] >= end_time:
        cnt = cnt + 1
        end_time = time_table[i][1]

print(cnt)