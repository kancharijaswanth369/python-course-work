c = 4 + 3j
print(type(c))
s = 'jaswanth'
r = 'sarath'
print(type(s))
print(type(r))
l = ['gopal','rishi','hemanth','rasool']
print(type(l))
z = ['1','string',3.14,[1,2,3],False]
print(type(z))
z.append(True)
print(z)
k = ()
print(type(k))
t = tuple() #by using constructor
print(type(t))
t = (1,'string')
# in a dictionary we don't have key duplicates
d = {}
d = dict()#using constructor
d = {'name':'jaswanth','batch':'30','course':'python'}
print(d)
w = set()#only way to declare a set is using constructor
w = {1,2,3,3,4}
print(w)
#set is unordered we cannot access using index
#list and tuple are ordered we can access using index
y = set()
y = {1,2,3,3,4}
y.add(5)
print(y)
