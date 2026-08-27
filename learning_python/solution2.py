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

def converter(usd_val):
   inr_val = usd_val * 96
   print(usd_val, "USD =", inr_val, "INR")


converter(100)