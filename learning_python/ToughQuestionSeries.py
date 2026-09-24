# The longest consecutive sequence

# numbers = [100, 4, 500, 29, 85, 1, 3, 2]

# num_set = set(numbers)
# longest = 0

# for num in num_set:

#     if num - 1 not in num_set:

#         current = num
#         length = 1

#     while current + 1 in num_set:
#         current += 1
#         length +=1

#     longest = max(longest,length)

# print(longest)

# Maximum subarray sum

# numbers = [-2, 1, -3, 4, -1, 2, -4, 5, 3]
# current = numbers[0]
# maximum = numbers[0]

# for i in range(1, len(numbers)):

#     current = max (numbers [i], current + numbers[i])

#     maximum = max(maximum, current)

# print(maximum)

#WAP TO PRINT THIRD,FIFTH AND SEVENTH ELEMENT FROM A LIST
#USING ENUMERATE FUNCTION.

# l = [1, 2, 3, 4, 5, 6, 7, 8]

# for i, item in enumerate(l):
#      if i== 2 or i == 5 or i == 7:
#          print(item)


# longest palindrome substring

# text = "babad"

# longest = ""

# for i in range(len(text)):

#     for j in range(i + 1, len(text) + 1):

#         substring = text[i:j]

#         if substring == substring[::-1]:

#             if len(substring) > len(longest):
#                 longest = substring

# print(longest)

# all subarrays with given sum

# numbers = [1, 2, 3, 6, 2]
# target = 5

# for i in range(len(numbers)):

#     total = 0

#     for j in range(i, len(numbers)):
#         total += numbers[j]

#         if total == target:
#             print(numbers[i:j+1])

# majority element

# numbers = [32, 45, 76, 99, 57]

# candidate = None
# count = 0

# for num in numbers:

#     if count == 0:
#         candidate = num

#     if num == candidate:
#         count += 1

#     else:
#         count  -= 1

# print(candidate)

# Find two numbers whose sum is target

numbers = [2, 7, 11, 15]
target = 9

seen = {}

for num in numbers:

    required = target - num

    if required in seen:
        print(required, num)
        break

    seen[num] = True
    