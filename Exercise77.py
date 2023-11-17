nhi=input("Nhập số nhị phân: ")
thap=0
bac=len(nhi) - 1
for so in nhi:
  thap = thap + int(so) * 2 ** bac
  bac = bac - 1
print("Số thập phân tương ứng là:", thap)