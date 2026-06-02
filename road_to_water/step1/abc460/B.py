T = int(input())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    dx = x1 - x2
    dy = y1 - y2

    dist2 = dx * dx + dy * dy

    inner = (r1 - r2) ** 2
    outer = (r1 + r2) ** 2

    if inner <= dist2 <= outer:
        print("Yes")
    else:
        print("No")
