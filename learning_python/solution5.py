#WRITE A CLASS "CALCULATOR" CAPABLE OF FINDING SQUARE,CUBE
# AND SQUARE ROOT OF A NUMBER.

class calculator:
    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"The square is {self.n*self.n}")

    

a = calculator(5)
a.square 