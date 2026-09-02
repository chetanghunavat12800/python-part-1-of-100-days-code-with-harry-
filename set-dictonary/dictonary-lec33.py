# lets talk about the dictonary in python 
dic1={
  "Name" : "Chetan meena",
  "Age": 19,
  'College': 'IIIT BHOPAL',
  "Branch": "Computer science and engineering"
}

print(dic1["Name"],dic1["Age"],dic1["College"],dic1["Branch"])
print(dic1)

dic2={
  11:"Chetan meena",
  45:"Mahima khandelwal", 
  34:"Rajpal yadav",
  24:"warren buffet"
}
print(dic2)

# -------------------------------------------------

info={"name": "chetan meena",
      "age": 19,
      "eligible": True
     }

print(info.keys())
print(info.values())


for key in info.keys():
  print(info[key])

print(info.items())

for key,values in info.items():
  print(f"the value corresponding to the key {key} is the   {values}")

for key,values in info.items():
  print(f"the value corresponding to the key {key} is the   {info[key]}")
    