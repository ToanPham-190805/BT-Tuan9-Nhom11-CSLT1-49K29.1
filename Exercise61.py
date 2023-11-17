print("Enter values to find Average")
avg   = 0
i = 0

while True:
    n = int(input("Enter Number: "))
    
    if i == 0 and n == 0:
        print("Error")
        continue 
    elif i != 0 and n == 0:
        break
    
    avg += n
    i += 1
    
print("Average =",avg/i)