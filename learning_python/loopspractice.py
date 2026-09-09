#WAP TO FIND WHETHER A GIVEN NUMBER IS PRIME OR NOT.

# n = int(input("Enter a number:"))

# for i in range(2 , n):
#     if (n%i) == 0:
#         print("Number is not prime")
#         break

# else:
#     print("Number is prime")

n = int(input("Enter a number:"))

for i in range(1,21):
    print(f"{n} x {i} = {n * i}")
