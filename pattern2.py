# n = int(input())
# for i in range(n):
#     for j in range(i + 1):
#         print("*",end = ' ')
#     print()
# n = int(input())
# for row in range(n):
#     for col in range(n-row):
#         print("*",end = ' ')
#     print()
# for row in range(5):
#     for col in range(5-row-1):
#         print(' ',end = ' ')
#     for col1 in range(row + 1):
#         print("*",end = ' ')
#     print()
# for row in range(5):
#     for col in range(row):
#         print(' ',end = ' ')
#     for col1 in range(5 - row):
#         print('*',end = ' ')
#     print()
# n = int(input("Enter the size: "))
# for row in range(n):
#     for col in range(n):
#         if row == 0 or col == 0 or row == n - 1 or col == n - 1:
#             print("*",end = ' ')
#         else:
#             print(' ',end = ' ')
#     print()

# n = int(input("Enter the size: "))
# for row in range(n):
#     for col in range(n):
#         if row == 0 or col == 0 or row == n - 1 or col == n - 1 or row == n//2:
#             print("*",end = ' ')
#         else:
#             print(' ',end = ' ')
#     print()

n = int(input("Enter the size: "))
for row in range(n):
    for col in range(n):
        if row == 0 or row == n - 1 or row  == n - col - 1:
            print("*",end = ' ')
        else:
            print(' ',end = ' ')
    print()


