n = int(input("Enter number of messages"))
chat = {}
for i in range(n):
    name,message = input().split(':')
    if name in chat:
        chat[name].append(message)
    else:
        chat[name] = message
   

print(chat)
    