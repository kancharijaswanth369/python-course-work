data = {
    1234:{"pin":123,"current_balance":5000,"history":[]},
    5678:{"pin":123,"current_balance":4000, "history":[]},
    9076:{"pin":123,"current_balance":8000, "history":[]},
}
print("Welcome to ATM")
acc = int(input("Enter the account number: "))
pin = int(input("Enter the pin: "))
if acc in data and data[acc]["pin"] == pin:
    print("Login Successful")
    while True:
        print(''' \nATM MENU " 
        "1. Check Balance" 
        "2. Deposit" 
        "3. Withdraw" 
        "4. Transactions" 
        "5. Exit ''')
        ch = int(input("select the option: "))
        if ch == 1:
            print(f"Current balance : ₹ {data[acc]['current_balance']}")

        elif ch == 2:
            amount = int(input("Enter the amount to deposit: "))
            data[acc]["current_balance"] += amount
            data[acc]["history"].append(f"Deposited ₹{amount}")
            print(f"Successfully deposited ₹ {amount}")


        elif ch == 3:
            amount = int(input("Enter the amount to withdraw: "))
            if data[acc]["current_balance"] >= amount:
                data[acc]["current_balance"] -= amount
                data[acc]["history"].append(f"Withdrawn ₹{amount}")
                print(f"Successfully withdrawn ₹ {amount}")
            else:
                print("Insufficient balance")
        elif ch == 4:
            print("Transaction history")
            for i in data[acc]["history"]:
                print(f"- {i}")
            
        elif ch == 5:
            break
        else:
            print("Invalid Choice")
