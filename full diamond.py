n = 10
for i in range(2*n):
    if i < n:
        stars = n - i
    else:
        stars = i - n + 1

    print("*" * stars + " " * (2*(n - stars)) + "*" * stars)
