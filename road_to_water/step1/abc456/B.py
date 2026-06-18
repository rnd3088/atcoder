A = [list(map(int, input().split())) for _ in range(3)]

cnt = 0

for x in A[0]:
    for y in A[1]:
        for z in A[2]:
            if sorted([x, y, z]) == [4, 5, 6]:
                cnt += 1

ans = cnt / (6 * 6 * 6)
print(ans)