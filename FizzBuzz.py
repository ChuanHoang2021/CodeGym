nhap = input('Nhập vào 2 số bất kỳ cách nhau = khoảng trắng: ')
c = nhap.split()
a, b = int(c[0]), int(c[1])
if b<a: print('số kết thúc cần lớn hơn số bắt đầu')
else:
    for i in range(a, b+1):
        if i%3==0 and i%5==0: print('FizzBuzz')
        elif i%3==0: print('Fizz')
        elif i%5==0: print('Buzz')
        else: print(i)
