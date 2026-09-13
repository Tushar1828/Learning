#FIBONACCI SERIES
# n = int(input("Enter number of terms :"))

# a = 0
# b = 1

# for i in range(n):
#     print(a, end=" ")
#     a, b = b, a + b


#practice higher values
# n = int(input("Enter a number series: "))

# a = 10
# b = 20

# for i in range(n):
#     print(a, end=" ")
#     a, b = b, a + b


#Swap two numbers

# a = int(input("Enter first number : "))
# b = int(input("Enter second number : "))

# a, b = b, a

# print("After swapping:")
# print("a =", a)
# print("b =", b)

# find common elements between two lists.

# list1 = [1, 2, 3, 4, 5]
# list2 = [3, 4, 5, 6, 7]
# # list3 = [1, 3, 4, 7]
# common = list(set(list1)& set(list2)& set(list3))

# print(common)

#Find missing number from a list.

# numbers = [1, 2, 3, 4, 5, 6]

# n = 6
# expected = n* (n + 1) //2

# actual = sum(numbers)
# missing = expected - actual
# print("Missing numbers:", missing)


# numbers = [299, 399, 499, 599]

# n = 3
# expected = n*(n+1) // 2

# actual = sum(numbers)

# missing = expected - actual
# print("Missing numbers:", missing)

class students:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math

    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math) / 3) + "%"

stu1 = students(56, 87, 96)
print(stu1.percentage)

stu1.phy = 45
print(stu1.percentage)