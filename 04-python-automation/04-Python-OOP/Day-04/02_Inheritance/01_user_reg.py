class User:

    def login(self):
        print("Login")

    def register(self):
        print("Register")


class Student(User):

    def enroll(self):
        print("enroll")

    def review(self):
        print("Review")


std = Student()
register = User()

register.register()
std.review()
std.enroll()
std.login()
std.register()



