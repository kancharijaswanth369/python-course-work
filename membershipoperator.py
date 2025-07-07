n = 'Jaswanth'
print('a' in n)
print('e' in n)
print('i' in n)
print('o' in n)
print('u' in n)

names = ['jaswanth','revanth','rahul','manideep','rahul','nikhil']
print('rahul' in  names)
s = { 1,2,3,4,5}
print(2 in s)
t = (1,2,3)
print(1 in t)
data = {'name' : 'jaswanth','batch' : 30, 'domain':'py'}
print('age' in data)
print('name' in data)
print('age' not in data)
print('in result:', 'rahul' in names) 
print('not in result:','chintu'in names)

#Identity operators
l = [1,2,3,4]
b = [1,2,3,4]
print(l is b)
a = b
print(a is b)
print(id(l))
print(id(b))
print(id(a))
print(a is not b)
print(l is not b)
#bitwise operators
print(3 & 5)#and operator
print(4|5)#or operator
print(5^6)#xor operator
print(~1)#not operator which will invert all the bits
#shift operators
print(2<<1)#left shift operator
print(4>>1)#right shift operator