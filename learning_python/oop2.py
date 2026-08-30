#DELETE

# class students:
#     def __init__(self,name):
#         self.name = name

# s1 = students("tushar")
# print(s1.name)
# del s1.name
# print(s1.name) 

#BASIC CONCEPT
class persons:
    __name = "anonymous"

    def __hello(self):
        print("hello person!")
    def welcome(self):
        self.__hello()
p1 = persons()

print(p1.welcome())