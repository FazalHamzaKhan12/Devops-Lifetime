class Atm:
    def __init__(self):
        self.pin = ""
        self.balance = 0
        
        self.menu()
    def menu(self):
        user_input = input("""
                            hello, i would to proceced?
                            1.Enter 1 to create pin
                            2.Enter 2 to Deposit
                            3.Enter 3 to withdrawl
                            4.Enter 4 to check balance
                            5.Enter 5 to exit
                        """)
        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.withdrawl_process()
        elif user_input == "3":
            self.deposit_process() 
        elif user_input == "4":
            self.check_balance()
        elif user_input == "5":
            print("bye sir/mam")
        else:
            print("invalid activity ")

    def create_pin(self):
        self.pin = input("enter your pin sir/mam: ") 
        print(f"Pin Successfully set")
    
    def deposit_process(self):
        temp = input("Enter your pin")
        if temp == self.pin:
            ammount =  int(input("Enter the amount "))
            self.balance + ammount
            print("Deposit Successfully")
        else:
            print("Enter Correct Pin, it's invalid")
    
    
    def withdrawl_process(self):
        temp = input("Enter your pin")
        if temp == self.pin:
            ammount =  int(input("Enter the amount "))
            if ammount < self.balance:
                self.balance = self.balance - ammount
                print("Operation successfull")
            else:
                print("insufficent funds")
        else:
            print("invalid Pin")
    
    def check_balance(self):
        temp = input("Enter your pin")
        if temp == self.pin:
            print(self.balance)
        else:
            print("invalid pin")
ubl = Atm()