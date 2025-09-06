rows = 5
for i in range(1, rows ):
    for j in range(1, rows ):
        if j <= i:
            print(j, end=' ')
        else:
            print(' ', end=' ')
    print()
# n=5
# for i in range(n):
#     for j in range(n-i):
#         print(j+1, end=" ")
#     print()