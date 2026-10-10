class Parent:

    def show_parent(self):
        print("Parent method")


class Child(Parent):

    def show_child(self):
        print("Child method")


obj = Child()

obj.show_parent()   # Inherited
obj.show_child()    # Own method