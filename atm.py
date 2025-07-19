print("Welcome to ATM")
n = int(input("Enter your account number:"))
k = int(input("Enter your PIN:"))
if n == 12345 and k == 9:
    print("Login Successful")
    transactions = {}
    balance = 5000.0
    while True:
        print("ATM Menu")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. View Transactions")
        print("5. Exit")
        balance = float(input())
        ch = int(input("Enter your Choice (1-5):"))
        if ch == 1:
            print(f"Your current balance : {balance}")
        elif ch == 2:
            print(f"your deposited amount: {}")
    


