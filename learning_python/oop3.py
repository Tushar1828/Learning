#INHERITANCE
#SINGLE / MULTI-LEVEL INHERITANCE
class car:
    @staticmethod
    def start():
        print("car is starting")

    @staticmethod
    def stop():
        print("car is stopping")

class toyota(car):
    def __init__(self, brand):
        self.brand = brand

                    
class fortuner(toyota):
    def __init__(self, brand):
        self.brand = brand

car1 = fortuner("diesel")
car1.start()         