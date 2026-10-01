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
    

# a = calculator(10)
# a.Hey()
# a.square ()
# a.cube()
# a.squareroot()

# Find longest substring containing only unique characters.


# text = "zzxxxccc"

# seen = set()
# left = 0
# longest = 0

# for right in range(len(text)):

#     while text[right] in seen:
#         seen.remove(text[left])
#         left +=1

#     seen.add(text[right])

#     longest = max(longest, right - left + 1)

# print(longest)

#Parking Management System

class vehicle:

    def __init__(self, number):
        self.number = number

class parking:

    def __init__(self, total_slots):
        self.total_slots = total_slots
        self.slots = {}

    def park_vehicle(self, vehicle):

        if len(self.slots) >= self.total_slots:
            print("Praking Full")
            return

        slot = 1

        while slot in self.slots:
            slot += 1

        self.slots[slot] = vehicle

        print(vehicle.number, "parked at slot", slot)

    def remove_vehicle(self, number):

        for slot, vehicle in self.slots.items():

            if vehicle.number == number:

                del self.slots[slot]

                print(
                    number,
                    "removed from slot",
                    slot
                )

                return

        print("Vehicle not found")  

        def show_slots(self):

         print("\nParking Status:")

        for slot in range(1, self.total_slots + 1):

            if slot in self.slots:
                print("Slot",slot,"->",self.slots[slot].number)

            else:
                print("slot", slot,"-> Empty")

parking = parking(3)

v1 = vehicle("JH01AB5748")
v2 = vehicle("JH01CD3087")

parking.park_vehicle(v1)
parking.park_vehicle(v2)

parking.show_slots()

parking.remove_vehicle("JH01AB5748")

parking.show_slots()  
