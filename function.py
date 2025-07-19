# def function_name(parameters):
#     #block of code

# function_name()
# all_status = True
# def send(reel_link,instaid):
#     if all_status:
#         print('send')
#         print('seen')
#         print('pending')

# def display(password,username,email):
#     print(username,email,password)
# name,email,pwd = 'rushi','rushi@gmail.com','rushi@123'
# display(name,email,pwd)
# def greet(name, age):
#     print(f"Hello {name}, you are {age} years old.")

# greet("Alice", 25) #positional arguments
# def add(*numbers):
#     return sum(numbers)


# print(add(1, 2, 3, 4, 5))
# print(add(3,4,5))
# print(add(2,3,4,5)) # variable length arguments

def user_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")



user_info(name="Alice", age=25, city="New York")
user_info(name = "Jayanth", age = 27, city = "London",status = "Alive") #variable keyword arguments




