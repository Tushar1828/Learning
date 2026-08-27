#def calc_sum(a , b):
   # return a + b

#sum = calc_sum(100, 490)
#print(sum)

#AVGERAGE OF 3  NUMBERS

#def calc_avg(a, b, c):
 #   sum = a + b + c
  #  avg = sum / 3
    #if(n ==  0):
#print(avg)
   # return avg

#calc_avg( 45, 76 , 90)

#RECURSIVE FUCNTION
def show(n):
    if (n == 0):
        return
    print(n)
    show(n - 1)

show(5)

#factorial
def fact(n):
    if (n == 1 or n == 0):
        return 1
    return fact(n-1) * n
print(fact(9))