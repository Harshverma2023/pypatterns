'''
    *-------*
    *-----*
    *---*
    *--*
    *- *
    '''
n=5    
for i in range(n):
    for j in range(1,n-1):
        print("_")
        if j == 0 or j == n - i - 1:
            print("*", end=" ")
        else:
            print("_", end=" ")