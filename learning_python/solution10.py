#FIBONACCI SERIES
# n = int(input("Enter number of terms :"))

# a = 0
# b = 1

# for i in range(n):
#     print(a, end=" ")
#     a, b = b, a + b


#practice higher values
# n = int(input("Enter a number series: "))

# a = 10
# b = 20

# for i in range(n):
#     print(a, end=" ")
#     a, b = b, a + b


#Swap two numbers

# a = int(input("Enter first number : "))
# b = int(input("Enter second number : "))

# a, b = b, a

# print("After swapping:")
# print("a =", a)
# print("b =", b)

# find common elements between two lists.

# list1 = [1, 2, 3, 4, 5]
# list2 = [3, 4, 5, 6, 7]
# # list3 = [1, 3, 4, 7]
# common = list(set(list1)& set(list2)& set(list3))

# print(common)

#Find missing number from a list.

# numbers = [1, 2, 3, 4, 5, 6]

# n = 6
# expected = n* (n + 1) //2

# actual = sum(numbers)
# missing = expected - actual
# print("Missing numbers:", missing)


# numbers = [299, 399, 499, 599]

# n = 3
# expected = n*(n+1) // 2

# actual = sum(numbers)

# missing = expected - actual
# print("Missing numbers:", missing)

# class students:
#     def __init__(self, phy, chem, math):
#         self.phy = phy
#         self.chem = chem
#         self.math = math

#     @property
#     def percentage(self):
#         return str((self.phy + self.chem + self.math) / 3) + "%"

# stu1 = students(56, 87, 96)
# print(stu1.percentage)

# stu1.phy = 45
# print(stu1.percentage)



# Move all zeros to the end

# numbers = [0, 2, 0, 39, 0, 67, 0]

# result = []

# for num in numbers:
#     if num != 0:
#         result.append(num)

# zeros = len(numbers) -len(result)

# for i in range(zeros):
#     result.append(0)

# print(result)

# Find the majority element

# numbers = [2, 2, 1, 1, 1, 2, 2]

# count = 0
# candidate = None

# for num in numbers:

#     if count == 0:
#         candidates = num

#     if num == candidate:
#         count += 1

#     else:
#         count -= 1

# print(candidate)     

# Rotate a list by k positions   

# numbers = [1, 2, 3, 4, 5]

# k = 2

# k = k % len(numbers)

# result = numbers[-k:] + numbers[:-k]

# print(result)

# numbers = [45, 54, 67, 86, 98,  40]
# k = 4

# k = k % len(numbers)

# result = numbers[-k:] + numbers[-k:]

# print(result)
# the first non-repeating character

# numbers = [1, 1, 2, 3, 4, 4, 3]

# for ch in numbers:
#     if numbers.count(ch) == 1:
#         print(ch)
#         break

#Find the missing number
#Numbers are from 1 to n.

# numbers = [1, 2, 3, 4, 5, 6]

# n = len(numbers) + 1

# total = n * (n + 1) // 2
# actual = sum(numbers)

# missing = total - actual

# print(missing)

# Find two numbers whose sum equals the target.

# numbers = [2 , 7 , 11, 16]
# target = 9

# seen = {}

# for i in range(len(numbers)):
#     required = target - numbers[i]

#     if required in seen:
#         print([seen[required], i])
#         break 

#     seen[numbers[i]] = i

# maximum subarray sum -- (kadane's Algorithm)
# numbers = [-2 , 1 , -3, 4, -1, 2, 1, -5, 4]

# current = numbers[0]
# maximum = numbers[0]

# for i in range(1, len(numbers)):
#     current = max(numbers[i], current + numbers[i])
#     maximum = max(maximum, current)

# print(maximum)

# first repeated character

# text = "programming"

# for ch in text:
#     if text.count(ch) > 1:
#         print(ch)
#         break



#Minimum subarray sum
# numbers = [ 1,-2, -3, 5]

# current = numbers[0]
# minimum = numbers[0]

# for i in range(1 , len(numbers)):
#     current = min(numbers[i], current + numbers[i])
#     minimum = min (minimum, current )

# print(minimum)   


# Second Largest Number without sort()

numbers = [10, 5, 20, 8, 25]

largest = float('-inf')
second =float('-intf')

for num in numbers:
    