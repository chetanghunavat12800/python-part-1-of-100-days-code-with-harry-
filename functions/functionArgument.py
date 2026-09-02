def findevenorodd(a=9): #a=9 is here the default argument 
  if(a%2==0):
    print("even")
  else:
    print("odd")



findevenorodd()

def average(a=1,b=5):
  print("average = ",(a+b)/2)

average(a=1)
average(b=5)
average()
average(a=3,b=5)

def findGreater(a,b): # here the a,b are required arguments...kyuki mai yha koi default val nhi de rha 
  if(a>b):
    print("a is greater than b ")

  elif(a<b):
    print("b is greater than a ")

  else:
    print("a is equal to b....a=b ")

findGreater(4,7)# this is not the key arg..
findGreater(a=4,b=7) # a=.. b=..   yeh sab key arguments hai
findGreater(b=4,a=7)



# variable length arguments.....

   #arbitary arguments..
print("i love you ")
def printNames(*waah):
  print("hello",waah[0],waah[1],waah[2])
  print(type(waah))
    
 

printNames("chetan","ramesh","ayush")

def printSurname(**waah):
  print("hello",waah["n1"],waah["n2"],waah["n3"])


printSurname(n1="chetan",n2="ramesh",n3="ayush")
