MOD = 998244353

S = input()

ans = 0
length = 1

for i in range(1, len(S)):
    if S[i] != S[i - 1]:
        length += 1
    else:
        ans += length * (length + 1) // 2
        length = 1

ans += length * (length + 1) // 2

print(ans % MOD)