#define a circle class with a radius r using the constructor.
#define area() method of the class which calculates the area of the circle .
# define perimeter() method of the class which allows you to calculate the perimeter of the circle.

# class circle:
#      def __init__(self, radius):
#           self.radius =  radius

#      def area(self):
#           return 3.14 * self.radius ** 2

#      def perimeter(self):
#           return 2 * 3.14 * self.radius

# c1 = circle(21)
# print(c1.area())
# print(c1.perimeter ())

# create a class called order which stores item & its price.
# use dunder funtion..gt..() to convey that:
# order1> order2 if price of order1>price of order2

class order:
    def __init__(self, item , price):
        self.item = item
        self.price = price

    def __gt__(self, odr2):
        return self.price > odr2.price


odr1 =  order("milshake", 160)
ord2 = order("coffee", 159)

print( odr1 > ord2)

          