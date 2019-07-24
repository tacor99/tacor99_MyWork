# coding: utf-8

from random import randint
k=randint(1,10)
a=0
while a!=k :
    b=input('請猜一個1-10的數字：')
    a=int(b)
print('你猜對!!!')
