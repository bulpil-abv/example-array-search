class Goat:
    age = 0
    name = ""
    weight = 0.0

    def show(self):
        print(self.name)
        print(self.age)


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(name, "+")


a = Goat()
print(type(a))
a.name = "Jolly"
a.age = 2

b = Goat()
print(type(b))
b.name = "Nelly"
b.age = 3
b.leg=5

a.show()
print(b.leg)

