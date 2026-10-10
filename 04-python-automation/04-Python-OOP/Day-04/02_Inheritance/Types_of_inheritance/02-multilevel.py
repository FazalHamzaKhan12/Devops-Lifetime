class GrandParent:

    def grand_method(self):
        print("Grandparent")


class Parent(GrandParent):

    def parent_method(self):
        print("Parent")


class Child(Parent):

    def child_method(self):
        print("Child")


obj = Child()

obj.grand_method()
obj.parent_method()
obj.child_method()