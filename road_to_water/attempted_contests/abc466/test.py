N, M = map(int, input().split())

max_size = [-1] * M

for _ in range(N):
    color, size = map(int, input().split())

    max_size[color - 1] = max(
        max_size[color - 1],
        size
    )

print(*max_size)