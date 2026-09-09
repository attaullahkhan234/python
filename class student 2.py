class student :
    grade = 10
    name = "John"

    def introduction(self):
        print("hi i am a student")

    def details(self):
            print("My name is", self.name)
            print("I am in grade", self.grade)

ob = student()
ob.introduction()
ob.details()