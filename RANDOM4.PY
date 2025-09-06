'''* * * * * 
* * * * 
* * * 
* * 
* 
* * 
* * * 
* * * * 
* * * * *'''
n = 5
# Top half (decreasing)
for i in range(n, 0, -1):
    print("* " * i)

# Bottom half (increasing)
for i in range(2, n+1):
    print("* " * i)
