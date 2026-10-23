#continue evenNUMBER
#i= 1 
#while i <= 10:
   #if(i%2 !=0): 
    #   i += 1
     #  continue
   #print(i)
 #i+=1  

#range
#for i in range(100,0,-1):
 #   print(i)

#WAF TO CONVERT USD TO INR.

# def converter(usd_val):
#    inr_val = usd_val * 96
#    print(usd_val, "USD =", inr_val, "INR")


# converter(100)

# a number is an Armstrong number

# n = 199
# digits = str(n)
# total = 0

# for digit in digits:
#    total += int(digit) ** len(digits)

# if total == n:
#    print("Armstrong Number") 
# else:
#    print("Not Armstrong")

# the third-largest distinct element

nums = [10, 5, 20, 8, 15, 20]

unique = list(set(nums))
unique.sort(reverse=True)

if len(unique) >= 3:
    print(unique[2])
else:
    print("Not enough elements")