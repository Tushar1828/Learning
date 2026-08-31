#POLYMORPHISM

#print(99 + 99)

#print("tushar" + "sharma")
#print([12,48] + [38, 90])

class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real,"i +", self.img,"j")

num1 = complex(1, 3)
num1.showNumber()

num2 = complex(4, 9)
num2.showNumber()
