 #function to find the  lcm of two nums
def LCM(a,b):
  # finding lcm
 i=1
 while(i%a!=0 or i%b!=0):
   i=i+1

 return i

a=int(input("enter the num1 : "))
b=int(input("enter the num2 : "))
LCM(a,b)

import math

# a=12
# b=18
# lcm = (a*b)//math.gcd(a,b)
# print(lcm)
print(math.lcm(a,b))




