a = 30
b = 40
c = 10
#comparision operators
print(a == b)
print(a != b)
print(a <= b)
print(a <= c)
print(a >= c)
#Assignment operators
a+=10
print(a) # add and assign
b*=10
print(b) # multiply and assign
c-=10
print(c) # subtract and assign

a /= 10 #divide and assign
print(a)

b //= 10 #floor and assign which will give only integer value
print(b)

b %= 10 # modulo and assign
print(b)

#Logical Operators

follower = True
public = False
canview = (follower == True or public == True)
print(canview)

x = 10
y = 40
print(x%10 == 0 and y%10 != 0)
print(x%10 == 0 or y%10 != 0)

