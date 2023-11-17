import math
x1=float(input("Nhập x:")) 
y1=float(input("Nhập y:"))
cvi= 0
x2=x1
y2=y1 
while True:
    x = input("Nhập x (trống thì dừng)):")
    if x =="":
        break
    x2 = float(x)
    y2 = float(input("Nhập y:"))
    kcach = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)  
    cvi=cvi+kcach
    x1=x2
    y1=y2    
kcach=math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
cvi=cvi+kcach
print("Chu vi của đa giác bằng:",cvi)