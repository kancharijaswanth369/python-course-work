# def fact(n):
#     if n == 1:
#         return 1
#     return n * fact(n - 1)
# n = int(input("Enter the value"))
# print(fact(n))
# n = int(input("Enter the value"))
# def sumofnumbers(n):
#     if n == 1:
#         return 1
#     return n + sumofnumbers(n-1)
# print(sumofnumbers(n))
# n = int(input("Enter the value"))
# def sumofdigits(n):
#     if n == 0:
#         return 0
#     return n % 10 + sumofdigits(n//10)
# print(sumofdigits(n))
n = int(input("Enter a number: "))
a,b = 0,1
for i in range(n):
    print(a,end = ' ')
    a,b = b,a+b
    