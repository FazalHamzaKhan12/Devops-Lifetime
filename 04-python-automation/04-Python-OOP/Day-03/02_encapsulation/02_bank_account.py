class BankAccount:

    def __init__(self):
        self.__balance = 8000
        self.__accountNumber = 12345

    def get_balance(self):
        return self.__balance

    def set_balance(self, newbalance):
        if newbalance >= 0:
            self.__balance = newbalance
            print("Balance changed")
        else:
            print("Invalid amount")

    def show_account(self):
        print(self.__balance)
        print(self.__accountNumber)


ubl = BankAccount()

ubl.show_account()

print(ubl.get_balance())

ubl.set_balance(23)

ubl.show_account()