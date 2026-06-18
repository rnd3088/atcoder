N, K = map(int, input().split())

A = []

for _ in range(N):
    row = list(map(int, input().split()))
    A.append(row[1:])

C = list(map(int, input().split()))

cur = 0

for i in range(N):
    block = len(A[i]) * C[i]

    if cur + block < K:
        cur += block
    else:
        pos = (K - cur - 1) % len(A[i])
        print(A[i][pos])
        break
