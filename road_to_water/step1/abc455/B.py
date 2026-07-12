H, W = map(int, input().split())

S = [input() for _ in range(H)]

ans = 0

for r1 in range(H):
    for c1 in range(W):
        for r2 in range(r1, H):
            for c2 in range(c1, W):

                ok = True

                for r in range(r1, r2 + 1):
                    for c in range(c1, c2 + 1):
                        rr = r1 + r2 - r
                        cc = c1 + c2 - c

                        if S[r][c] != S[rr][cc]:
                            ok = False

                if ok:
                    ans += 1

print(ans)