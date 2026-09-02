#  yeh baat yaad rkho string is immutable
   #jo bhi ho rha hai uski copy banti hai 
name="chetan"
print(len(name))
print(name)
print(name.upper()) # converts in uppercase 
print(name.lower())  # converts in lowercase 
name2="!!!!chetan!!!!!"
print(name2.rstrip("!")); # right se hta do !
print(name2.lstrip("!"));  #left se hta do  !
print(name2.strip("!"));   # string se ! hts do
print(name2.replace("chetan","ayush"))   #replace chetan by ayush
name3="chetan meena !!!!"
print(name3.split(" "))   # it convert string in list  for string where it seperated by space 

### capitalize
str1="CHetan Is a gOOd bOy, yEs"
str2=str1.capitalize()  # make first letter of string to the capital
print(str2)

str3="welcome to rajasthan"
print(str3.center(2*len(str2)))
print(str3.endswith("rajasthan"))

# .....count a particular str occurences 
str4="once upon a time there was a crow one day crow was very thirsty the crow was in search of the water ."
n=str4.count("crow")
print(n)

print(str4.find("thirsty"))
print(str4.index("thirsty"))

str5="Chetan Meena The Legend"
print(str5.istitle())   

print(str5.swapcase())  

untitle1="the ultimate Goal OF tHe lIfe ."
print(untitle1.title())
