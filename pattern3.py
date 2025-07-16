n = int(input())
for row in range(n):
    for col in range(n):
        if row == 0 or row == n - 1 or row == n - col - 1 or row == col:
            print("*",end = ' ')
        else:
            print(" ",end = ' ')
    print()
