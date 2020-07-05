# thêm r trước chuỗi để vô hiệu hóa kí tự
print(r'haz, \neu mot ngay nao do')
print('haz, \neu mot ngay nao do')
strA= "HowKteam"
strB= "Free education"
strC = strA + "\n" + strB
print(strC)
strD = (strA + "\n")*5
print(strD)
# toán tử 'in' kiểm tra chuỗi có nằm trong chuỗi hay không
strE = "K" in strA # chuỗi A có nằm trong strA nên trả về true
print(strE)
#lấy ra từng ký tự trong chuỗi
print(strA[3])
#Hàm len() lấy ra độ dài chuỗi
print(strA[len(strA)-1])
# cắt chuỗi
print(strA[1:6])
print(strA[None:6])
print(strA[5:None])
print(strA[None:None])
# cắt nhảy 2 đơn vị, cách 1 cắt 1
print(strA[None:None:2])
# cắt nhảy ngược 2 đơn vị ,cách 1 cắt 1
print(strA[None:None:-2])
#cắt ngược
print(strA[None:None:-1])
# ép kiểu dữ liệu vd int()
#kiểu dữ liệu phải phù hợp: như này là sai: int("6.9")
# A = int(6.9) -> 6
A= int("69") +5
B= 69+5
print(A)
print(B)
# ép kiểu từ số thành chuỗi
print(str(69) + "5")
# thay thế chữ o bằng số 0
C= strA[None:1] + "0" + strA[2:None]
print(C)
