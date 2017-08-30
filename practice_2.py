# -*- coding:utf-8 -*-

#设计一个程序返回100以内的所有素数列表
from math import sqrt
def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True
prime_list = []
for n in range(1,100):
    if is_prime(n):
       prime_list.append(n)
print(prime_list)
