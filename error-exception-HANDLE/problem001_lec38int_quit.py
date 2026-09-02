def printint():
  n=input('please enter the input as a integer ')

  if(n.lower()=='quit'):
    return 0

  elif(n!='1984'):
    raise ValueError ("the entered pin is INCORRECT")

x=printint()
 