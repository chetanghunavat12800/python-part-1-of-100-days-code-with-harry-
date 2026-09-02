# ...how i can edit the tuple .....#

tup1 = ("chetan meena", "08/09/2007", 19, "ckb", "swm", "RJ-25")
# if i want to add the rajasthan in the last of the tuple i cannot do it directly i can do it with the help of the list

temp = list(tup1)

temp.append("rajasthan")
tup1 = tuple(temp)
print(tup1)

#...................
tup2=(1,2,3,4,5,6,7,8)
tup2=(tup2[2:7])
print(tup2)

# finding the index of req. element

tup3=(1,2,3,4,5,2,7,4,3,9)
idx=tup3.index(3)
print(idx)   #   this will give first occurence 
#if we want to find in a particular part of tuple 

idx1=tup3.index(3,4,9)#____.index(element,start,end)
print(idx1) 