# The longest consecutive sequence

numbers = [100, 4, 500, 29, 85, 1, 3, 2]

num_set = set(numbers)
longest = 0

for num in num_set:

    if num - 1 not in num_set:

        current = num
        length = 1