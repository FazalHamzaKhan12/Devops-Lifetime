class Phone:

    def buy(self):
        print("buying a phone")

class Smartphone(Phone):

    def buy(self):
        print("buying a smartphone")

        super().buy()


s = Smartphone()

s.buy()