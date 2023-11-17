tong=0
count=0
while True:
    diemchu=input("Đánh giá điểm:")
    if diemchu=="":
        break
    elif diemchu=="A":
        tong=tong+4
    elif diemchu=="B+":
        tong=tong+3.5
    elif diemchu=="B":
        tong=tong+3
    elif diemchu=="C+":
        tong=tong+2.5
    elif diemchu=="C":
        tong=tong+2
    elif diemchu=="D+":
        tong=tong+1.5
    elif diemchu=="D":
        tong=tong+1
    elif diemchu=="F":
        tong=tong+0
    count=count+1
print("Điểm trung bình:",round(tong/count,2))