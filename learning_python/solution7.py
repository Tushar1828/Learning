#LIST COMPREHENSION

# mylist = [4, 6, 8, 3, 0]

# squaredlist = []
# for item in mylist:
#     squaredlist.append(item*item)

# print(squaredlist)

#WAP TO PRINT THIRD,FIFTH AND SEVENTH ELEMENT FROM A LIST
#USING ENUMERATE FUNCTION.

l = [1, 2, 3, 4, 5, 6, 7, 8]

for i, item in enumerate(l):
    if i== 2 or i == 5 or i == 7:
        print(item)
