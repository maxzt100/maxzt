class Student:
    amount_of_students = 0

    def __init__(self, name=None, height=160):
        self.name = name
        self.height = height
        Student.amount_of_students += 1

    def __str__(self):
        return f"I am a student {self.name} with height {self.height}"

    def printer(self):
        print(self.height)

    def grow(self, height=1):
        self.height += height


nick = Student(name="Nick")
print(nick.height)
kate = Student(height=170)
print(kate.height)
print(kate.amount_of_students)
print(Student.amount_of_students)
nick.printer()
nick.grow()
print(nick.height)
nick.grow(height=15)
print(nick.height)
print(nick)

