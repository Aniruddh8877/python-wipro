# Bank Transaction System

def display_menu():
    print("\n----- Bank Transaction Menu -----")
    print("1. Deposit Money")
    print("2. Withdraw Money")
    print("3. Check Balance")
    print("4. Exit")
    print("----------------------------------")

def main():
    balance = 500  
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':  
            amount = float(input("Enter amount to deposit: "))
            balance += amount
            print(f"Amount deposited successfully. New balance = {balance}")

        elif choice == '2':
            amount = float(input("Enter amount to withdraw: "))
            if amount <= balance:
                balance -= amount
                print(f"Withdrawal successful. New balance = {balance}")
            else:
                print("Insufficient funds.")

        elif choice == '3': 
            print(f"Current balance = {balance}")

        elif choice == '4': 
            print("Thank you for using our banking system!")
            break

        else:
            print("Invalid option. Please choose between 1–4.")

if __name__ == "__main__":
    main()
