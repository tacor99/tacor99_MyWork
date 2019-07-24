# coding: utf-8
st='23,68,99'
s=st.split(',')
k=[]
for i in st.split(','): 
    k.append(int(i))
print(k)
print(k)
sum=0
for i in k:
    sum=sum+i
print(sum)
a=['A','B','C','D','E','F']
k=len(a)
b=[]
for i in a:
    k=k-1
    b.append(a[k])
print(b)
    
s1='ABCDEFGHIJK'
n=len(s1)

s2=''
for i in range(1,n+1):
    s2=s2+s1[-i]
print(s2)
def reverse(s):
    return s[::-1]
reverse(['a','b','c','d'])
reverse('abcdefghijkl')

from random import randint
k=randint(1,10)
a=0
while a!=k :
    b=input('請猜一個1-10的數字：')
    a=int(b)
print('你猜對!!!')
