'''
4. 
1  
1 *  
1 * 3  
1 * 3 *  
1 * 3 * 5 
'''
n = int(input("Enter the value of n: "))
for i in range(1, n + 1):
    row = ""
    for j in range(1, i + 1):
        if j % 2 == 1:
            row += str(j) + " "
        else:
            row += "* "
    print(row)