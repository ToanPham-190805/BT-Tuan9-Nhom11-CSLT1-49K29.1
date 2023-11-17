while True:
  bit=input("Nhập chuỗi 8 bit (nhập rỗng để thoát):")
  if bit=='':
    break
  if len(bit)!=8:
    print("Bạn phải nhập chính xác 8 bit")
    continue
  bit=str(bit)
  count=0
  for i in range(1,9):
      j=bit[i-1]
      if j=="1":
        count=count+1
  if count % 2 == 0:
    print("Bit parity là 0")
  else:
    print("Bit parity là 1")