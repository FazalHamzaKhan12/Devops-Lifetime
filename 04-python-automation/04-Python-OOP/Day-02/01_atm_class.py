class Atm:
    def __init__(self):
        self.pin = ""
        self.balance = "0"

        self.menu()

    def menu(self):
        user_input = ""

        while user_input != "5":

            user_input = input("""
            
                Hello, how would you like to proceed?
                1. Create PIN
                2. Deposit
                3. Withdraw
                4. Check balance
                5. Exit
                
                """)

            if user_input == "1":
                self.create_pin()

            elif user_input == "2":
                self.deposit_process()

            elif user_input == "3":
                self.withdrawl_process()

            elif user_input == "4":
                self.check_balance()

            elif user_input == "5":
                print("Bye sir/mam")

            else:
                print("Invalid activity")

    def create_pin(self):
        self.pin = input("Enter your PIN: ")
        print("PIN successfully set")

    def deposit_process(self):
        temp = input("Enter your PIN: ")

        if temp == self.pin:
            amount = int(input("Enter the amount: "))
            self.balance += amount
            print("Deposit successful")

        else:
            print("Incorrect PIN")

    def withdrawl_process(self):
        temp = input("Enter your PIN: ")

        if temp == self.pin:
            amount = int(input("Enter the amount: "))

            if amount <= self.balance:
                self.balance -= amount
                print("Operation successful")

            else:
                print("Insufficient funds")

        else:
            print("Invalid PIN")

    def check_balance(self):
        temp = input("Enter your PIN: ")

        if temp == self.pin:
            print(f"Your balance is: {self.balance}")

        else:
            print("Invalid PIN")


ubl = Atm()