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

numbers = [-2, 1, -3, 4, -1, 2, -4, 5, 3]
current = numbers[0]
maximum = numbers[0]

for i in range(1, len(numbers)):

    current = max (numbers [i], current + numbers[i])

    maximum = max(maximum, current)

print(maximum)