x=float(input("Nhập số cần tìm căn bậc 2:"))
guess=x/2  
while True:
  guess=(guess + x/guess)/2
  if abs(guess**2 - x)<=10**(-12):
    break  
print(guess)