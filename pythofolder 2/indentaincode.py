a=int(input("enter the num1: "))
b=int(input("enter the num2: "))
c=a+b
if(c>0):
       print("sum is positive")
elif(c==0):
       print("sum is zero")

elif(c<0):
  print("yes")
  if(c<-10 and c>-20):
    print("c lies b/w 10 and -20",c)
  elif(c<-20):
    print("c is less than -20",c)
        
  