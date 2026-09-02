l=["chetan meena",20,"ckb","swm",25]
print(l)
l.append("rajasthan")   #append adds at the last of the list
print(l)
l.reverse()

print(l)

list1=[7,4,3,8,6,7,4,9,0,4]
list1.sort()
print(list1)
list1.reverse()
print(list1)
print(list1.index(0))
print(list1.count(4))

#.......copy list ........
list2=[1,2,3,4,5,6,7]
m=list2.copy()   
print(m)
m[0]=8
print(list2)
print(m)
#............yha ref. ke through copy ho rha hai 
reflist=list2
print(reflist)
reflist[0]=69
print(list2)
print(reflist)
list2.insert(3,89)
print(list2)

h=[45,56,67]
list2.extend(h)
print(list2)

#.......concatenate two lists....

list3=[0,9,8,7,6,5]
list4=[4,3,2,1]
list5=list3+list4

print(list5)




list6=[1,2,3,4,5,6,7,8]
list6=list6[2:7]
print(list6)