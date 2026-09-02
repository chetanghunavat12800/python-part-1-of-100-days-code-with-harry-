def fact(n):
    if n == 0 or n == 1:
        return 1

    return n * fact(n - 1)

def sum_(a):
  '''
  please input the numbers in the list []
  '''
  return sum(a)

def sqrt(a):
  
  if(a<0):
    raise ValueError('Domain error please enter valid input under domain')

  return a**(1/2)

def cbrt(a):
  if(a<0): 
    a=-a
    a=a**(1/3)
    return -a
  return a**(1/3)

def floor(a):
  return a//1

def ceil(a):
  if(type(a)==int):return a
  return (a//1)+1

def hypot(l,b):
  return ((l*l)+(b*b))**(1/2)

def average(l):
  if(len(l)==0): return 0
  return (sum(l)/len(l))


