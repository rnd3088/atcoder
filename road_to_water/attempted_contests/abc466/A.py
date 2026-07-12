N = int(input())
X = list(map(int, input().split()))

if all(value < 0 for value in X):
    print("Yes")
else:
    print("No")
