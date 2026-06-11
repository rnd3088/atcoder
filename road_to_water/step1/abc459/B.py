n = int(input())
s = input().split()

ans = ""

for word in s:
    c = word[0]

    if c in "abc":
        ans += "2"
    elif c in "def":
        ans += "3"
    elif c in "ghi":
        ans += "4"
    elif c in "jkl":
        ans += "5"
    elif c in "mno":
        ans += "6"
    elif c in "pqrs":
        ans += "7"
    elif c in "tuv":
        ans += "8"
    else:
        ans += "9"

print(ans)