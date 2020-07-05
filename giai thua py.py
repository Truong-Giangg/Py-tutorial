print ('chuong trinh tinh giai thua giai thua')
def giaithua(n):
			if n == 1:
				return 1
			else:
				return (n*giaithua(n-1))
num = 5
#num1 = int(input("nhap so can tinh giai thua"))
print("Giai thua cua", num,"la", giaithua(num))
