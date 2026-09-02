a=int(input("enter the first num: "))
b=int(input("enter the second num: "))
print("press 1 to add them. \npress 2 to subtract them. \npress 3 to multiply them. \npress 4 to divide them. ")
choice=int(input("enter your choice:"))

if choice==1:
    print("the sum of the two numbers is: ",a+b)

elif choice==2:
  print ("the difference of the two numberss is: ",a-b)
elif choice==3:
  print("the product of the two numbers is: ",a*b)
elif choice==4:
  print("the division of the two numbers is: ",a/b)
else:
  print("INVALID CHOICE")


  
  