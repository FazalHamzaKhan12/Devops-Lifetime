class ATM_machine:
    def __init__(self):
        self.menu()
        
    def menu(self):
        user_Input = int(input("""
        Hello, I Would to Proceced?
        1.Enter 1 to create pin
        2.Enter 2 to Deposit
        3.Enter 3 to withdrawl
        4.Enter 4 to check balance
        5.Enter 5 to exit : \n
                          """))
        if 1 == 1:
            print("Enter Your Pint SIR!")
        elif 2 == 2:
            print("Enter Your Deposit Fund")
        elif 3 == 3:
            print("Enter Money TO Witdrawal")
        elif 4 == 4:
            print("Check the balance")
        elif 5 == 5:
            print("Good bye!")
        else:
            print("invalid Activitly")
        
        
ubl = ATM_machine()
ATM_machine.menu()