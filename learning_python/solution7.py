#LIST COMPREHENSION

# mylist = [4, 6, 8, 3, 0]

# squaredlist = []
# for item in mylist:
#     squaredlist.append(item*item)

# print(squaredlist)

#WAP TO PRINT THIRD,FIFTH AND SEVENTH ELEMENT FROM A LIST
#USING ENUMERATE FUNCTION.

# l = [1, 2, 3, 4, 5, 6, 7, 8]

# for i, item in enumerate(l):
#     if i== 2 or i == 5 or i == 7:
#         print(item)

#MULTIPLICATIONS

# n = int(input("Enter a number:"))

# table = [n*i for i in range(1, 11)]
# print(table) 

#WAP TO DISPLAY A/B WHERE A AND B ARE INTEGERS.
#IF B=0, DISPLAY INFINITE BY HANDLING THE'ZERODIVISIONERROR'.

# try:
#     a = int(input("Enter a: "))
#     b = int(input("Enter b: "))
#     print(a/b)
# except ZeroDivisionError as v:
#     print("Infinite") 
# 
#STORE THE MULTIPLICATION TABLES GENERATED IN PROBLEM 3 IN A FILE NAMED TABLES.TEXT.

n = int(input("Enter a number:"))

table = [n*i for i in range(1, 111)]
with open ("tables.txt", "a") as f:
    f.write(str(table) + "\n")
