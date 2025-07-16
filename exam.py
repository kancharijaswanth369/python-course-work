# date = input().split('-')
# date = date[::-1]
# print('/'.join(date))
# date,month,year = input().split('-')
# print(f'{year}/{month}/{date}')
# n = input()
# n.replace('a','*')
# n.replace('e','*')
# n.replace('i','*')
# n.replace('o','*')
# n.replace('u','*')
# print(n)
# n = input().lower()
# print(n.translate(str.maketrans('aeiou','*****')))
# credentials = ("admin","python123")
# username = input()
# password = input()
# if username == "admin" and password == "python123":
#     print("login succesful")
# else:
#     print("unsuccessful")
# n = set(input().split(','))
# print(sorted(n))
# n = int(input())
# data = {}
# max_val = 0
# res = ''
# for i in range(n):
#     name,mark =  input().split()
#     mark = int(mark)
#     if mark > max_val:
#         res = name
#     data[name] = mark

# print(data)
# print(name)
# n = input().split()
# for i in range(len(n)):
#     n[i] = n[i][::-1]
# print(' '.join(n))
# n = list(map(int,input().split()))
# res = []
# for i in n:
#     if i != 0:
#         res.append(i)
# print(res)
n = input()
res = {}
for i in n:
    if i not in res and i!= ' ':
        res[i] = n.count(i)
print(res)


