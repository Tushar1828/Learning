# class students:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#         print("adding new students in database")

# s1 = students("tushar",50)
# print(s1.name,s1.marks)

# s2 = students("ali",49)
# print(s2.name,s2.marks)

# Method Overriding

class Animal:
    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def sound(self):
        print("Dog barks")

animal = Animal()
dog = Dog()

animal.sound()
dog.sound()