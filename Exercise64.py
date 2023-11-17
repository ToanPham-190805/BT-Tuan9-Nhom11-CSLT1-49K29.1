tong = 0
while True:
    gia = input("Nhap gia:")
    if gia == "":
        break
    tong = tong+float(gia)
    tong=float(tong)
print("Tong la:",round(tong,2))
xu = round(tong * 100)
du = xu % 5
if du < 2.5:
    ttoan = tong - du / 100  
else:
    ttoan = tong + (5 - du) / 100
print("So tien phai thanh toan la:",round(ttoan,2))