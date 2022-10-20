import sys
input = sys.stdin.readline

N = int(input())


triangle = []
# 2차원리스트로 받는다
for _ in range(N):
    triangle.append(list(map(int, input().split())))


for i in range(1, N):
    # triangle 리스트형원소 안을 순회한다.
    for j in range(len(triangle[i])):

        # 제일 밑에 줄 (triangle 의 제일 끝에 원소 리스트)에 두 대각선을 더하면서 내려온 값들이 담기게 된다.

        if j == 0:
            triangle[i][j] = triangle[i][j] + triangle[i-1][j]
        elif j == i:
            triangle[i][j] = triangle[i][j] + triangle[i-1][j-1]
        else:
            triangle[i][j] = triangle[i][j] + max(triangle[i-1][j-1], triangle[i-1][j])

# 마지막 인덱스원소 안에 원소중에서 제일 큰 값을 출력한다.

print(max(triangle[N-1]))




