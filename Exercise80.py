import random 
total = 0 
for i in range(10):
    f1 = random.choice(['H', 'T'])
    f2 = random.choice(['H', 'T'])
    f3 = random.choice(['H', 'T'])
    print(f1, f2, f3, end = ' ')
    flip = 3
    while True:
        if f1 == f2 == f3:
            break 
        else:
            flip += 1 
            f1 = f2
            f2 = f3
            f3 = random.choice(['H', 'T'])
            print(f3, end = ' ')      
    print('(' + str(flip) + ' flips)')
    total += flip 
print('On average,', total / 10, 'flips were needed')
