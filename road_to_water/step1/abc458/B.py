h, w = map(int, input().split())

for i in range(h):
    row = []

    for j in range(w):
        count = 0

        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni = i + di
            nj = j + dj

            if 0 <= ni < h and 0 <= nj < w:
                count += 1

        row.append(count)

    print(*row)
