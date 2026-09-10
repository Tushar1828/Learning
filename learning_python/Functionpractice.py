#WAP USING FUNCTIONS TO FIND GREATEST OF THREE NUMBERS.
# def greatest(a, b, c):
#     if(a>b and a>c):
#         return a
#     elif(b>a and b>c):
#         return b
#     elif(c>b and c>a):
#         return c

# a = 100
# b = 199
# c = 299
# print(greatest(a, b, c))

#WAP PROGRAM USING FUCNTION TO COVERT CELSIUS TO FAHRENHEIT.

# def f_to_c(f):
#  return 5*(f-32)/9   
# f = int(input("Enter temperature in F:"))


# print(f"{f_to_c(f)} °C")

#WRITE A RECURSIVE FUNCTION TO  CALCULATE THE SUM OF FIRST N NATURAL NUMBERS.

# def sum(n):
#     if(n==1):
#         return 1
#     return sum(n-1) + n
# print(sum(400))

#WAP FUNCTION WHICH CONVERTS INCHES TO CMS.

def inch_to_cms(inch):
    return inch *2.54

n = int(input("Enter value in inches:"))

print(f"The corresponding value in cms is {inch_to_cms(n)}")
