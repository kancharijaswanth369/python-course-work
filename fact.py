# n = int(input("Enter the number :"))
# fact = 1
# for i in range(1, n + 1):
#     fact = fact * i

# print(fact)
n = int(input("Enter the number: "))

for j in range(1,n + 1):
    fact = 1
    for i in range(1, j + 1):
        fact = fact * i

    print(f"{j} ! = {fact}")