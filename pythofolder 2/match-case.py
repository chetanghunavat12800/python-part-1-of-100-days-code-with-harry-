x=int(input("enter the value of x: "))
match x:
 case 1:
  print("case 1 operated ")
 case 2:
   print("case 2 operated ")
 case _ if(x!=55): #empty case with condition
    print(x,"is not equal to the 55")
  
 case _:
   print("default case")
     