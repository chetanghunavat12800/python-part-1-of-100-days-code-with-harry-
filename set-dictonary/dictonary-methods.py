  # add or update items in the dictonary

ep1={"sde":"chetan meena",
     "hde":"shashank tripathi",
     "it-e":"lokendra singh",
     "webd":"nitin dhawan",
     "cyber":"ronak patel",
     "app":"rudra smadhiya"
    }
print(ep1)
ep1["it-e"]="naitik sharma" 
ep1["alumni"]="adiya zala"
ep1.update({"hde":"subham mishra"})
ep1.update({"event manager":"pranav singh"})

for key in ep1:
  print(key,ep1[key],sep="-----")


 # removing the element from the dictonary
  # clear()   pop() popitem()
data2={
    "id01":"chetan",
    "id02":'lokendra',
    'id03':'abhay',
    'id04':'harish',
    'id05':'das'
}
data2.pop('id05')
print(data2)
data2.popitem()
print(data2)

# data2.clear() #this will clear the complete dictonary 
# print(data2)
del data2['id01']   # thi will key the provided key and data value
print(data2)

del data2  # this will delete the entire dictonary ....

 