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

# Find longest substring containing only unique characters.


text = "zzxxxccc"

seen = set()
left = 0
longest = 0

for right in range(len(text)):

    while text[right] in seen:
        seen.remove(text[left])
        left +=1

    seen.add(text[right])

    longest = max(longest, right - left + 1)

print(longest)