bank = {} 


def create_account():
    acc = input("Enter new Account Number: ")

    if acc in bank:
        print("Account already exists!")
        return

    name = input("Enter Account Holder Name: ")
    balance = float(input("Enter Initial Deposit: "))

    bank[acc] = {"name": name, "balance": balance}
    print("Account created successfully!\n")


def deposit():
    acc = input("Enter Account Number: ")

    if acc not in bank:
        print("Account not found!\n")
        return

    amount = float(input("Enter amount to deposit: "))
    bank[acc]["balance"] += amount
    print("Amount deposited!\n")


def withdraw():
    acc = input("Enter Account Number: ")

    if acc not in bank:
        print("Account not found!\n")
        return

    amount = float(input("Enter amount to withdraw: "))
    if amount > bank[acc]["balance"]:
        print("Not enough balance!\n")
        return

    bank[acc]["balance"] -= amount
    print("Amount withdrawn!\n")


def check_balance():
    acc = input("Enter Account Number: ")

    if acc not in bank:
        print("Account not found!\n")
        return

    print("Balance:", bank[acc]["balance"], "\n")


def view_accounts():
    if not bank:
        print("No accounts available.\n")
        return

    print("\n----- ALL ACCOUNTS -----")
    for acc, details in bank.items():
        print("Account Number:", acc)
        print("Name:", details["name"])
        print("Balance:", details["balance"])
        print("------------------------")
    print()


while True:
    print("===== BANK MENU =====")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. View All Accounts")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        create_account()
    elif choice == "2":
        deposit()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        check_balance()
    elif choice == "5":
        view_accounts()
    elif choice == "6":
        print("Thank you for using the Bank System!")
        break
    else:
        print("Invalid choice! Try again.\n")
