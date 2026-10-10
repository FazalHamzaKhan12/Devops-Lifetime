class Atm:

    def __init__(self):
        self.__pin = ""
        self.__balance = 0

        self.__menu()

    def get_pin(self):
        return self.__pin

    def set__pin(self,new__pin):
        if type(new__pin) == str:
            self.__pin = new__pin
            print("Pin Changed")
        else:
            print("Now Allowed")
    

    def __menu(self):
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
        self.__pin = input("Enter your PIN: ")
        print("PIN successfully set")

    def deposit_process(self):
        temp = input("Enter your PIN: ")

        if temp == self.__pin:
            amount = int(input("Enter the amount: "))
            self.__balance += amount
            print("Deposit successful")

        else:
            print("Incorrect PIN")

    def withdrawl_process(self):
        temp = input("Enter your PIN: ")

        if temp == self.__pin:
            amount = int(input("Enter the amount: "))

            if amount <= self.__balance:
                self.__balance -= amount
                print("Operation successful")

            else:
                print("Insufficient funds")

        else:
            print("Invalid PIN")

    def check_balance(self):
        temp = input("Enter your PIN: ")

        if temp == self.__pin:
            print(f"Your balance is: {self.__balance}")

        else:
            print("Invalid PIN")


Atm()

# ubl.get_pin()