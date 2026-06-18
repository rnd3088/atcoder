S = input()
N = len(S)

ans = 0

for i, ch in enumerate(S):
    if ch == "C":
        ans += min(i, N - 1 - i) + 1

print(ans)