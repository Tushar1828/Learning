#create student class that takes name & marks of 
#3 subjects as arguments in constructor  then create a method to print the avg.

class students:
    def __init__(self, name, marks):
        self.name = name 
        self.marks = marks

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hi", self.name, "your avg score is:",sum/3)

s1 = students("tushar",[50,60,70])        
s1.get_avg()

