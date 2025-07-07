Python 3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> print("Addition of two numbers")
Addition of two numbers
>>> a = 10
>>> b = 20
>>> c = 30
>>> print("Addition",a + b)
Addition 30
>>> print("
...       
SyntaxError: unterminated string literal (detected at line 1)
>>> print("Subtraction", a - b)
...       
Subtraction -10
>>> print("Multiplication", a * b * c)
...       
Multiplication 6000
>>> print("Power", a ^ b)
...       
Power 30
>>> print("Value" a ** b)
...       
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print("Value", a ** b)
...       
Value 100000000000000000000
>>> a = []
...       
>>> a.append(10)
...       
>>> a.append(20)
...       
>>> print('a')
...       
a
>>> return a
SyntaxError: 'return' outside function
>>> print(a)
[10, 20]
