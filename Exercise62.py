print('Discount is 60%')
print()
for i in (4.95, 9.95, 14.95, 19.95, 24.95):
    
    print('Original price =',i)
    
    j=i*0.4

    print('Discounted price =', round(i-j,2))
    print()
    print("_" * 20)