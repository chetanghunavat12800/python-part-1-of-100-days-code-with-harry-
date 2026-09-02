for i in range(0,6):
  print(i)
  if(i==1):
    print(i)
    break
else:
  print('hahaha')

print('loop over ho gya ')

numbers = [10, 20, 30, 40]
target = 20

for num in numbers:
    if num == target:
        print("Found!")
        break
else:
    print("Not Found!")  