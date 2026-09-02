
import time
timestamp=time.strftime('%H:%M:%S')
print(timestamp)
t=time.strftime('%H%M%S')
if(t>='050000' and t<"120000"):
  print("good morning sir ")

elif(t>='120000' and t<'160000'):
  print("good afternoon sir")

elif(t>='160000' and t<'190000'):
  print("good evening sir")

elif(t>='190000' and t<'240000' ):
  print("good night sir ")

else:
  print("good night sir")


  
