# how to raise the custom error in the python 
# if we want to fetch the four digit pin=1984
n=int(input("enter the pin for transaction"))
if (n!= 1984):
  raise ValueError ("your pin does not matching ")

else: 
  print("you entered ")