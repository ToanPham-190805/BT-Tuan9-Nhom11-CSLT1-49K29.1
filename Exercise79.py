import random
max = random.randint(1, 100) 
count = 0
print(max)
for i in range(99):
  num = random.randint(1, 100)
  if num > max:
    max = num
    count = count + 1
    print(num,'<== Update')
  else:
    print(num)
print()  
print('Max:', max)
print('Updates:', count)