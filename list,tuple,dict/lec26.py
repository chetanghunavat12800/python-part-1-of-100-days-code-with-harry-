import random
# name =["chetan",'ayush','vivek','kartik',"gaurav","anu","tina","seema","anita","mahaveer"]
a=input("please enter your name :")
idx=random.randint(0,9)

funny_names = [
    "Potato King",
    "WiFi Chor",
    "Drama Factory",
    "Maggi Master",
    "Lazy Legend",
    "Mr. Buffering",
]

print("hey",a,"you are a ",funny_names[idx])

