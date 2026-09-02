# ------------------------------------------------------
# add the data by curly braces
str1 = "my name is {} and iam from country {}"
name = "chetan meena"
country = "india"
print(str1.format(name, country))

str2 = "mera naam {1} hai and mai {0} se hu "
naam = "chetan meena"
sehar = "swm"
print(str2.format(country, name))
print("-" * 50)
# ------------------------------------------------------

# here we are using now f- string


str3 = "once upon a time my name is {} i was eating {}"
name = "chetan"
food = "icecream"
str4 = f"once upon a time my name is {name} i was eating {food}"

print(str4)

price = 29.7878897
print(f"the is approxly {price:.3f} ")



#-----------------------------------------------
print("-" * 50)
def square(n):
  '''it takes n as a input and return square of the n 
  '''
  square=n**2
  print(square)

square(5)
print(square.__doc__) 