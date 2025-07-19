print("printing w")
n = int(input())
for i in range(n):
    for j in range(n):
        if j == 0 or j == n - 1 :
            print('*',end = ' ')
        elif i >= n//2 and(i==j or j == n- i -1):
            print('*',end = ' ')
        else:
            print(' ',end = ' ')
    print('')
