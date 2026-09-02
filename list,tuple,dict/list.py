#......list are changable........but tuples cannot be change .......


l=[1,2,3]
print(l)
print(l[0])
print(l[1])
print(l[2])

list1=["chetan meena","cse",6]
print(list1)

print(list1[0])
print(list1[1])
print(list1[2])
if 6 in list1:
  print("yes 6 is present ")

else:
   print("no 6 is not present ")

print(list1[1:2])
list2=["chetan","ayush",19,14,"bhopal","jaipur",462022,302012,"MP04","RJ14","♥","☺"]
print(list2[0:len(list2):2])

print(list2[1:len(list2):2])


#.....list comprehensin.....

names=["chetan","ayush","vivek","kartik","anu","tina",'gaurav','seema','anita','mahaveer']
namelenmore5=[i for i in names if (len(i)>5)]
print(namelenmore5)

nameswithu=[j for j in names if "u" in j]
print(nameswithu)


classnames=["chetan meena","ishan gupta","vaibhav jain","kushal meena","sachin meena","gaurav sen","piyush meena","kapil sharma","rajpal yadav","amitabh bachhan","tushar meena"]
names_meena=[naam for naam in classnames if "meena" in naam ]
