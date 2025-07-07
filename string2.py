name = 'Mahesh babu is a great actor'
print(name.find('Mahesh'))
print(name.find('a'))
print(name.rfind('a'))
print(name.index('a'))
print(name.rindex('a'))
print(name.find('z'))
print(name.count('a'))

#String Testing methods
print('PFS30'.startswith('PFS'))
l = ['psf20','pfs30','pfs31','pfs32','jfs30','ds30']
for i in l:
    if i.startswith('pfs'):
        print(i)
    if i.endswith('30'):
        [print(i)]
k = ['demo.png','resume.pdf','index.webp','add.py','mul.py','div.py']
for i in k:
    if i.endswith('png'):
        print(i)
print(name.isalpha())
Name = 'Jaswanth'
print(Name.isalpha())
Digit = "12345"
print(Digit.isdigit())
print(Name.isdigit())
alphanumeric = 'jaswanth116'#contains only alphabets and numericals if any special symbols also it returns false
print(alphanumeric.isalnum())
print(alphanumeric.islower())
print(Name.islower())
print(name.islower())
Set = 'JASWANTH'
print(Set.isupper())
print(name.isspace())
K = " "
print(K.isspace())
word = 1
for i in name:
    if i.isspace():
        word += 1
print(word)
name1 = name.title()
print(name1)
print(name1.istitle())
print('1'.isdecimal())
print('2.34445'.isdecimal())
print('1.234'.isnumeric())
print('myvar'.isidentifier())
print('name'.isidentifier())
print(name.isidentifier())
#replace and modify methods
print(name.translate(str.maketrans("abou","zy%6")))
print('abcdef'.translate(str.maketrans("abcdef",'******')))
print(name.replace("Mahesh","prabhas"))

#splitting and joining methods
print(name.split())
print(name.split('a'))
print(name.rsplit('a'))
print(name.rsplit(' ',2))# in this rsplit('separator',how many times which means and iterator stops after 2 spaces from right side but it displays from left to right)
string = 'Jaswanth'
print(len(string))
print(max(string))#based on ascii value
print(min(string))#based on ascii value
print(sorted(string))#based on ascii value
print(ord('J'))
print(ord('A'))
print(ord('a'))
print(ord('@'))
print("python".maketrans("aon","#!@"))
z = 'Hello\nwelcome\neveryone'
print(z.splitlines())
print(''.join(z))
print(' '.join(z))
