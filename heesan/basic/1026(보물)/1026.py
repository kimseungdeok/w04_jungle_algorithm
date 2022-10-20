import sys

input = sys.stdin.readline

n = int(input())

alis = list(map(int, input().split()))

blis = list(map(int, input().split()))


alis.sort()
blis.sort()
blis.reverse()

sum = 0
for i in range(n):
    result = alis[i] * blis[i]
    sum = sum + result

print(sum)
