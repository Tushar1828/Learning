#WRITE A CLASS "CALCULATOR" CAPABLE OF FINDING SQUARE,CUBE
# AND SQUARE ROOT OF A NUMBER.

# class calculator:
#     def __init__(self, n):
#         self.n = n

#     def square(self):
#         print(f"The square is {self.n*self.n}")

#     def cube(self):
#         print(f"The cube is {self.n*self.n*self.n}")

#     def squareroot(self):
#         print(f"the squareroot is  {self.n**1/2}")

#     @staticmethod
#     def Hey():
#         print("Hey Buddy!")
    

# a = calculator(5)
# a.Hey()
# a.square ()
# a.cube()
# a.squareroot()

#write a class train which has method to book,
#get status and get fare inforamtion of train running underinidian railways.

from random import randint

class Train:

    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self, fro, to):
        print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to}")

    def getstatus(self):
        print(f"Train no: {self.trainNo} is running on time ")

    def getFare(self, fro, to):
        print(f"Ticket fare in train no: {self.trainNo} from {fro}to {to} is{randint(22, 5555)}")

t = Train(12806)
t.book("Ranchi", "Delhi")
t.getstatus()
t.getFare("Ranchi", "Delhi")
