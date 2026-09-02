#------union of sets...............
s1={1,2,3,6,8}
s2={4,6,5,7,2,7}
s3=s1.union(s2)
print(s3)
print(s2.union(s1))
s2.update(s1)   # s2 ko update kr do and s2 mai vo values dall do jo s2 mai nhi hai and s1 mai hai 
print(s1,s2)
#----------------------------------------------------
#------intersection of sets...............
s3={1,3,6,8,9,4}
s4={2,5,6,3,0}

print(s3.intersection(s4))

s3.intersection_update(s4) #s3 se vo val hta do jo s4 mai nahi hai 
print(s3,s4)

#-----------------------------------------------------

# symmetric difference in sets
set1={'jaipur','delhi','agra','bhopal','kota','swm'}
set2={'delhi','bhopal','mathura','gwalior','agra','sikar'}
print(set1.symmetric_difference(set2))
set1.symmetric_difference_update(set2)
print(set1)


#  difference in set

cities1={'jaipur','delhi','agra','bhopal','kota','swm'}
cities2={'delhi','bhopal','mathura','gwalior','agra','sikar'}
 
print(cities1.difference(cities2))  # print those values which are in cities1 but not in cities2

print(cities2.difference(cities1))  # print those values which are in cities2 but not in cities1

cities1.difference_update(cities2)
print(cities1)



# disjoint set hai ya nahi
cities1={'jaipur','agra','bhopal','kota','swm',23,True,}
cities2={'delhi','mathura','gwalior','sikar',False}
print(cities1.isdisjoint(cities2))  # does set1 and set2 have distinct elements  ?

# superset--------------
country1={'india',"russia",'germany','poland','veitnam','pakistan','nepal','bhutan',"monaco"}
country2={'india','poland','veitnam','monaco','russia'}

print(country1.issuperset(country2))
print(country2.issubset(country1))


# add and remove the element in the set 

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.add("india")
print(cities)

cities_2={'pakistan','russia','nepal','hungary'}
cities.update(cities_2)
print(cities)


  #remove/ discard---The main difference between remove and discard is that, if we try to delete an item which is not present in set, then remove() raises an error, whereas discard() does not raise any error.
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.remove('Berlin')
print(cities)
cities.discard('Tokyo') 
print(cities)

diff_countries1 = {"India", "Japan", "China", "Brazil", "Canada", "Australia", "Germany", "France", "Italy", "Russia", "Mexico", "South Africa", "Egypt", "Nepal", "Argentina"}
countries_disc={ "Canada", "Australia","Egypt", "Nepal",}
diff_countries1.difference(countries_disc)
print(diff_countries1.difference(countries_disc))
  
 
# pop and delete

cities_ = {"Tokyo", "Madrid", "Berlin", "Delhi"}
item = cities_.pop()
print(cities_)
print(item) 

cities__ = {"Tokyo", "Madrid", "Berlin", "Delhi"}
del cities__
#  print(cities__)  ....thiis gives an error in the console
cities_best = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities_best.clear()
print(cities_best)

#-------------------
info = {"Carla", 19, False, 5.9}
if "Carla" in info:
    print("Carla is present.")
else:
    print("Carla is absent.")
