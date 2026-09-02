# x=4
# def funct():
#   x=9  # this is not the global variable this local variable 
#   print(x)

# funct()
# print(x) #this will print the global variable 

# print('-'*25)

# y= 5

# def funct2():
#   global y # this tells the function that this is the global variable
#   y=8  # here we changed the value of the global varibale 
#   print(y)   # this prints the global variable 


# funct2()
# print(y)   # this also  prints the global variable 

z=3
def funct3(z):
  z=6
  print(z)


funct3(z)
print(z)