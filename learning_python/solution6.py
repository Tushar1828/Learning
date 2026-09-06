#create a class (2-D vector) and use it to create another 
#class representing a 3-D vector.

# class Twovector:
#     def __init__(self, i, j):
#         self.i = i
#         self.j = j

#     def show(self):
#         print(f"The vector is {self.i}i + {self.j}j")

# class Thirdvector(Twovector):
#     def __init__(self, i, j, k):
#         super().__init__(i, j)
#         self.k = k

#     def show(self):
#         print(f"The vector is {self.i}i + {self.j}j + {self.k}")  

# a = Twovector(1, 2)
# a.show()
# b = Thirdvector(1, 2, 3)
# b.show()         

# CREATE A CLASS 'EMPLOYEE' AND ADD SALARY AND INCREMENT PROPERTIES TO IT.
#WAM 'SALARYAFTERINCREMENT' METHOD WITH A @PROPERTY DECORATOR WITH A SETTER WHICH CHANGES THE VALUE OF INCREAMNETY BASED ON THE SALRY.

class Employee:
    salary = 456
    increment = 30

    @property
    def salaryAfterIncrement(self):
        return (self.salary + self.salary * (self.increment/100))

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, salary):
        self.increment = ((salary/self.salary) -1)*100


e = Employee()
e.salaryAfterIncrement = 690
print(e.increment)