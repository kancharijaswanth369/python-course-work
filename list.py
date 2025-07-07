a = []
a.append(10)
a.append(20)
a.append(30)
a.append(31)
print(a)
for i in range(len(a)):
    if a[i] % 2 == 0:
        print("even")
    else:
        print("odd")
l = [1,2,3,4,5]# list is ordered
#list is mutuable which means we can change
print(l)
l = [1,1,2,3,4,5]#list contains duplicates
print(l)
l = ['banana','apple','orange']
print(l[0])#list throught indexing
print(l.append('watermelon'))
l.extend([2.3,"string",[4,5],{'name':'jaswanth'},{1,3,4},(1,4,9),False,(2+4j)])#which means it is a heterogenous because it contains all types data types which means it contains dictionaries,tuples,complex,set etc..
print(l)
l.remove('apple')
print(l)
my_list = ['python','java','cpp','c']
print(my_list[-1])
print(my_list[-4])
print(my_list[::-1])
k = [1,2,3,1,5,6,7,8,9,23,27]
print(k.count(1))
print(sorted(k))
print(k)
print(k.sort())
print(k)
#the difference is sorted and sort is sorted is for temporary purpose where as sort modifies original array or list
k.insert(1,2)
print(k)