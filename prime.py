n = int(input("Enter the number"))
count = 0
for i in range(1,n + 1):
    if n % i == 0:
        count += 1

print(count)
if count == 2:
    print("The Number is a prime number")
else:
    print("The number is not a prime number")
#the above code is simple code we have to think for optimal code
#the below code is better code
fact = 0
k = int(input("Enter the number"))
for j in range(2,(k//2) + 1):
    if k % j == 0:
        fact += 1
print(fact)
if fact == 1:
    print(f"{k} is a prime number and it has {fact + 1} factors")
else:
    print(f"{k} is not a prime number and it has more than two factors")