from collections import Counter

N, M = map(int, input().split())
F = list(map(int, input().split()))

cnt = Counter(F)

print("Yes" if max(cnt.values()) == 1 else "No")
print("Yes" if len(cnt) == M else "No")