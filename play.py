import random
print('1.Rock')
print('2.Paper')
print('3.Scissors')
while True:
    ch = int(input("Enter your choice(0-Exit): "))
    if ch == 0:
        print("Game Over")
        break
    elif ch == 1:
        com = random.randint(1,3)
        if com == 1:
            print("Computer Choice: ",com)
            print("It's a tie")
        elif com == 2:
            print("Computer Choice: ",com)
            print("computer wins")
        elif com == 3:
            print("Computer Choice: ",com)
            print("You Win")

    elif ch == 2:
        com = random.randint(1,3)
        if com == 1:
            print("Computer Choice: ",com)
            print("You Win")
        elif com == 2:
            print("Computer Choice: ",com)
            print("It's a tie")
        elif com == 3:
            print("Computer Choice: ",com)
            print("Computer wins")
    elif ch == 3:
        com = random.randint(1,3)
        if com == 1:
            print("Computer Choice: ",com)
            print("Computer wins")
        elif com == 2:
            print("Computer Choice: ",com)
            print("You Win")
        elif com == 3:
            print("Computer Choice: ",com)
            print("It's a tie")
    else:
        print("Invalid Choice give me the correct choice")
for i in range(10):
    print(random.randint(1,3))
