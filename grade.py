
data = {
    1:{'Name':'Dinesh','exam_status':True,'python':100,'sql':95,'html':98},
    2:{'Name':'Arun','exam_status':True,'python':900,'sql':45,'html':60},
    3:{'Name':'Kireet','exam_status':False,'python':None,'sql':None,'html':None},
    4:{'Name':'Avinash','exam_status':True,'python':100,'sql':95,'html':98},
    5:{'Name':'Shyam','exam_status':True,'python':100,'sql':95,'html':98}
    
}
for i in data.keys():
    print(f'{i}.{data[i]["Name"]}')

stuid = int(input("Enter the student id: "))
if stuid in data:
    if data[stuid]['exam_status']:
        total = (data[stuid]["python"] + data[stuid]["sql"] + data[stuid][html])/3
        if total > 90:
            