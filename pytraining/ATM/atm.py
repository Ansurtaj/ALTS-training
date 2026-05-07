def deposit(balance):
    amount = float(input("Enter amount to deposit: "))
    if amount > 0:
        balance += amount
        print("Amount deposited successfully 👍")
    else:
        print("Invalid amount!")
    return balance


def withdraw(balance):
    amount = float(input("Enter amount to withdraw: "))
    if amount <= 0:
        print("Invalid amount!")
    elif amount > balance:
        print("Insufficient balance ❌")
    else:
        balance -= amount
        print("Please collect your cash 💵")
    return balance


def check_balance(balance):
    print("Current balance:", balance)


# Initial balance
balance = 1000  

while True:
    print("\n--- ATM MENU ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        balance = deposit(balance)

    elif choice == 2:
        balance = withdraw(balance)

    elif choice == 3:
        check_balance(balance)

    elif choice == 4:
        print("Thank you for using ATM 🙏")
        break

    else:
        print("Invalid choice! Try again.")