introduction="""Hello everyone, \nMy name is chetan meena. 
Iam a good Developer."""
skills="c and cpp and python languages. \nData structure and algorithm."

print(introduction)
print(len(introduction)) # len() function gives the length of the string ....
print(skills)
print((len(skills)))

# if we want to print the string till certain idx...
 # using [start:end] And for loop is another method....
print(introduction[0:15:2]) # start is included but the end is not included only 14 tk hi hoga
print(introduction[:15])  # 0 khud lga lega  python

#  slicing of str....
print(skills[2:10])
print(skills[:])

# Negative slicing
print(skills[2:-10])   # [2:len(skill)-10] ...negative ke aage len() lga leta h pyton
print(skills[-50:20])   # [len(skills)-5:20] ...negative ke aage len() lga leta h pyton

nm="Harry"
print(nm[-4:-2])
