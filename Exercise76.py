n=int(input('Enter an integer:'))
a=2
if n<=2:
    print('Error, Please re-enter.')
else:
    print('The prime factors of',n,'are:')
    while n>2:
        if n%a==0:
            print(a)
            n=n/a
        else:a=a+1
