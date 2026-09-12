#Remove duplicates from list
# numbers = [99, 99, 0, 0,101, 299, 499, 499]

# duplicates = []

# for num in numbers:
#     if num not in duplicates:
#      duplicates   .append(num)
# print(duplicates)

# numbers = [10, 20, 10,30 , 50]
# for i in range(len(numbers)):
#     print(i, numbers[i])

#Find frequency of each character.

# l = "Tushar"

# frequency = {}

# for character in l:
#     if character in frequency:
#         frequency[character] += 1
#     else:
#         frequency[character] = 1

# print(frequency)  
# using function

# def char_frequency(text):
#     frequency = {}

#     for char in text :
#         if char in frequency:
#             frequency[char] += 3
#         else:
#             frequency[char] = 2

#     return frequency

# print(char_frequency("Tushar"))   

#Check whether two strings are anagrams

# def check_anagram(str1,str2):
#     if sorted(str1)  ==sorted(str2):
#         print("Anagram")

#     else:
#         print("Not Anagram")

# print(check_anagram("listen","silent"))   "listen" = "eilnst"  "silent" = "eilnst"

#Easy method/ Placement-friendly

def is_anagram(a, b):
    return sorted(a) == sorted(b)

print(is_anagram("liten","silent"))

