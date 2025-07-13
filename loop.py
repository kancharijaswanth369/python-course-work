#dictionary
name = {1:'Jaswanth',2:'Rahul',3:'Nikhil',4:'Revanth'}
for i in name.keys():
    print(f"{i} - {name[i].capitalize()}")
#normal for loop
for i in range(1,21):
    print(f'2 * {i} = {2*i}')
#tuple
color = ('red','green','blue','yellow')
for i in color:
    print(i)
students = [("Jaswanth",21),("Manideep",21),("Rahul",69),("Surya",10)]
for name,age in students:
    print(f"Name: {name},Age: {age}")