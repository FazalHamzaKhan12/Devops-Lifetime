class Vehicle:

    def start(self):
        print("Vehicle Start")

    def stop(self):
        print("Vehicle Stopped")


class Car(Vehicle):

    def drive(self):
        print("Car is driving")

car1 = Car()

car1.drive()
car1.start()
car1.stop()