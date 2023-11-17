baby_price=0.00
children_price=14.00
adult_price=23.00
senior_price=18.00
babylimit=2
childlimit=12
adultlimit=64
s=0
n=input('The age of the guest (blank to finish): ')
while n!= "" :
    age=int(n)
    if age <= babylimit :
        s = s + baby_price
    elif age<= childlimit :
        s = s + children_price
    elif age<= adultlimit :
        s = s + adult_price
    else:
        s = s + senior_price
        
    n=input('The age of guest (blank to finish): ')
print ('The total for that group is $%.2f' %s)