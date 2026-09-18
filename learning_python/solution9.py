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

# def is_anagram(a, b):
#     return sorted(a) == sorted(b)

# print(is_anagram("listen","silent"))

# def check_anagram(str1, str2):
#       if sorted(str1) == sorted(str2):
#             print("Anagram")
#       else:
#             print("Not Anagram")

# print(check_anagram("care","race"))

# intersection of two arrays

# list1 = [1, 2, 2, 1, 1, 2, 1]
# list2 = [2, 2, 1, 1]

# result = []

# for num in list2:

#     if num in list1:
#         result.append(num)
#         list1.remove(num)

# print(result)

# Count Vowels and Consonants

# text = "python programming"

# vowels = 0
# consonants = 0

# for ch in text.lower():

#     if ch in "aeiou":
#         vowels += 1

#     elif ch.isalpha():
#         consonants += 1

# print("Vowels:", vowels)
# print("Consonants:", consonants)

# Q. find vowels and consonants in a sentence by its own 

text = input("Enter a string: ")

vowels = 0
consonants = 0

for ch in text.lower():

    if ch in "aieou":
        vowels += 1

    elif ch.isalpha():
        consonants += 1

print("vowels:", vowels)
print("consonants:", consonants)