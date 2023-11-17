m=int(input("Nhập số nguyên dương m: "))
n=int(input("Nhập số nguyên dương n: "))
if m > n: 
  d = n
else:
  d = m
while d > 0:
  if m%d==0 and n%d==0:
    break
  else:
    d=d-1
print("Ước chung lớn nhất của", m, "và", n, "là:", d)