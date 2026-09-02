def function1():
  try:
    a=int(input("enter the number "))
    li=['chetan','locky','abhay','shivam']
    print(li[a])
    return 1
  
  except Exception as e:
    print(e)
    return 0
  
  finally:
    print("finally gets executed....");

# calling the function:
x=function1()
print(x)