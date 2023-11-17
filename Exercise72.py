chuoi = input("Nhập vào một chuỗi: ")
do_dai = int(len(chuoi))
chuoi_nguoc = ""
for i in range(1,do_dai+1):
  chuoi_nguoc += chuoi[do_dai - i]
  i += 1
if chuoi == chuoi_nguoc:
  print(chuoi, "là một palindrome")
else:
  print(chuoi, "không phải là một palindrome")