# def say_hi():
#     print('hi')

# print('bye')
# say_hi()
# say_hi()
# say_hi()
# say_hi()

# def add_two_number():
#     a=int(input('nhap so thu nhat:'))
#     b=int(input('nhao so thu hai:'))
#     print('tong hai so la:'+str(a+b))
# add_two_number()

#   # viết hàm tên là evaluate, nhận vào 2 số và 1 phép tính. Tính toán 
    # phép tính này với 2 số đầu và trả về giá trị tínhd được:

#   # làm số nguyên tố bằng hàm cách của Thư
# from math import *
# def so_nguyen_to(n):
#     if n==1: 
#         return False
#     elif n==2 or n==3:
#         return True
#     else:
#         for i in range(2,round(sqrt(n))+1):
#             if n%i==0:
#                 return False
#     return True
# n=int(input('Enter N: '))
# print(so_nguyen_to(n))

#   # Cach cua thay

def is_prime(n):
    if n < 2:
        return False
    for v in range(2, int(n/2)):
        if n % v == 0:
            return False
    return True

# print(is_prime(101))

for v in range(1000,10000):
    if is_prime(v):
        print(v)