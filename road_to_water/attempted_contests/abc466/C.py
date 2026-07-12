N = int(input())

left = 1
right = 2
answer = 0

while right <= N:
    print("?", left, right, flush=True)
    response = input()

    if response == "Yes":
        right += 1
    else:
        answer += right - left - 1
        left += 1

        if left == right:
            right += 1

while left < N:
    answer += right - left - 1
    left += 1

print("!", answer, flush=True)
