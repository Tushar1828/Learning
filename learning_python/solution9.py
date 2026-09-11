#Remove duplicates from list
numbers = [99, 99, 0, 0,101, 299, 499, 499]

duplicates = []

for num in numbers:
    if num not in duplicates:
     duplicates   .append(num)
print(duplicates)
