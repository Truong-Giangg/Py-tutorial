a= 'My name is %s' %('Giang')
b= 'My name is %s %s' %('Giang', 'nè')
print(a)
print(b)
s= '%s %s'
result = s % ('1', '2')
print(result)
# kiểu số thực lấy 3 số sau dấu phẩy, làm tròn
t= '%.3f' % (3.9999)
print(t)
# chức năng của chữ f trong chuỗi

k= 'Kteam'
print (f'{k} - Free educaton')
print ('\t\t ví dụ f')
name ='Thao'
address= 'Da lat'
phone= '0157'
print(f'Tên: {name}\nĐịa chỉ: {address}\nSDT: {phone}')
# đặt thêm dấu ngoặc nhọn nếu muốn vô hiệu hóa chức năng của f
print(f'Tên: {{name}}\nĐịa chỉ: {address}\nSDT: {phone}')
print('\t\t Định dạng fomat')
print('a{}, b{}, c{}'.format(1,2,3))
# đánh số bằng cách nhập vào trong dấu ngoặc
print('a:{1}, b:{0}, c:{2}'.format('zezo','one','two'))
# có thể lấy 2 giá trị giống nhau, hoặc tạo 2 giá trị mà chỉ lấy 1
print('a:{0}, b:{0}, c:{2}'.format('zezo','one','two'))
print('a:{1}, b:{0}'.format('zezo','one','two'))
# có thể đặt tên chuỗi giống như f - string
print('a:{giang}, b:{mai}, c:{thao}'.format(giang ='zezo',thao= 'one',mai ='two'))
print('\t\t Căn lề bằng format')
# căn giữa
print('{:^50}'.format('Giang pro'))
# căn lề trái
print('{:<10}'.format('Giang pro'))
# căn lề phải
print('{:>70}'.format('Giang pro'))
# thay khoảng trắng là kí tự
print('Hello{:*>70} nè'.format('Giang pro'))
print('\t\t ví dụ format')
print('+ {:-<10} + {:-^10} + {:->10}'.format('','','') )
print('| {:<10} | {:^10} | {:>10} |'.format('ID', 'Ho va ten', 'Nam sinh'))
print('| {:<10} | {:^10} | {:>10} |'.format('01', 'Ngu Trung', '1000TCN'))
print('| {:<10} | {:^10} | {:>10} |'.format('02', 'Phò Đôn', '2000TCN'))
print('+ {:-<10} + {:-^10} + {:->10}'.format('','','') )