import string
chuoi = input("Nhập chuỗi: ")
chuoi = chuoi.replace(" ", "")
chuoi = chuoi.lower()
dau_cau = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
for ky_tu in dau_cau:
  chuoi = chuoi.replace(ky_tu, '')  
do_dai = len(chuoi)
chuoi_dao_nguoc = ""
i = 0
while i < do_dai:
  chuoi_dao_nguoc += chuoi[do_dai - 1 - i]
  i += 1
if chuoi == chuoi_dao_nguoc:
  print("Chuỗi là palindrome")
else:
  print("Chuỗi không phải là palindrome")