'''
題目說明：
n代表參加定時K彈的人數
從第一人依次傳遞一個炸彈
在第m人爆炸
要炸K次
問:最後一次爆炸的下一個人是幾位?

作法說明:
請輸入n m k三數, 中間以空白隔開:8 3 6（假設）
8個數字就形成8個環狀鍵結
每個list的第一個數字代表程式第16行的data
每個list的第一個數字代表程式第17行的next指向下一個位置8人
位置(list)編号分別是0, 1, 2, 3, 4, 5, 6, 7 
[1, 1] ->[2, 2] ->[3, 3] ->[4, 4] ->[5, 5] ->[6, 6] ->[7, 7] ->[8, 0]  ->[1, 1] 
再由環狀鍵結
去找每3人爆炸一次
共爆炸6次
進而找出
最後一次爆炸的下一個人是第4位

'''
temp1=input('請輸入n m k三數, 中間以空白隔開:')
temp2=temp1.split()
n=int(temp2[0])
m=int(temp2[1])
k=int(temp2[2])

temp4=[]
for i in range(n-1):    
    temp3=[]
    data=i+1
    next=i+1
    temp3.append(data)
    temp3.append(next)    
    temp4.append(temp3)
temp3=[]
temp3.append(n)
temp3.append(0)    
temp4.append(temp3)
count=0
current=0
pre=0
i=0
while i<k:
    count=count+1
    if (count==m):   
        temp4[pre][1]=temp4[current][1]
        i=i+1
        n=n-1
        count=0
    pre=current
    current=temp4[current][1]
print(temp4[current][0])
    
    
