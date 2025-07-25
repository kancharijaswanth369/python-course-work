# def evenorodd(n):
#     if n % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"
# n = int(input())
# print(evenorodd(n))
# n = int(input())
# iseven = lambda n: "Even" if n % 2 == 0 else "Odd"
# print(iseven(n))
# a = 20
# divl = lambda a,b = 3: a/b
# print(divl(a))
# def squares(l):
#     for i in range(len(l)):
#         l[i] = l[i] ** 2
#     return l
# l = [1,2,3,4,5]
# # print(squares(l))
# squ = list(map(lambda i: i ** 2,l))
# print(squ)
# l = 'python'
# vol = 'aeiou'
# squ = list(map(lambda i: '*' if i in vol else i,l))
# print(squ)
# l = [1,2,3,4,5,6,7,7,8,9]
# squ = list(filter(lambda i: i % 2 == 0,l))
# print(squ)
# l = [1,0,0,0,3,4,0,5,0,6,0,6]
# removed = list(filter(lambda i: i != 0,l))
# print(removed)
# from functools import reduce
# numbers = [1,2,3,4,5]
# sumall = reduce(lambda x,y:x+y,numbers)
# print(sumall)
# data = {'mouse':True,'laptop':False,'soap':True,'phone':False,'charger':True}
# d = list(filter(lambda i:i,data))
# print(d)
# data = {'mouse':True,'laptop':False,'soap':True,'phone':False,'charger':True}
# d = list(filter(lambda i:data[i],data))
# print(d)
data = {'dinesh': 47,'mukesh': 31,'gowtham': 45}
d = dict(sorted(data.items(),key = lambda i:i[0],reverse = True))
print(d)