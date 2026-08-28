class students:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("adding new students in database")

s1 = students("tushar",50)
print(s1.name,s1.marks)

s2 = students("ali",49)
print(s2.name,s2.marks)