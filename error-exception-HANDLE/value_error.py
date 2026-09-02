try:
  a=int(input("enter the num: "))
  nums=[1,2,3,4]
  print(nums[a])
  print(b)
except ValueError:
  print("here is the value error")

except IndexError as inde:
  print(inde)

except NameError as e:
  print(e)
  
