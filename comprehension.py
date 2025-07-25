# k = [i for i in range(1,11) if i % 2 == 0]
# print(k)
# k = { i for i in range(1,11) if i % 2 == 0}
# print(k)
# k = {i:i**2 for i in range(1,11)}
# print(k)
l = ['pen','book','pencil','eraser']
k = {i+1:l[i] for i in range(len(l))}
print(k)