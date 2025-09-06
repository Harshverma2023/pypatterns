num = int(input("Enter a starting number: "))
for i in range(1, 10):
    for j in range(num, num + i):
        print(j, end=" ")
    num += i
    print()
