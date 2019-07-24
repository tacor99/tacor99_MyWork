'''
給三角形三邊長
判斷三角形類型
'''
while True:
    x=input('請輸入三角形的整數三邊長, 並用空白鍵隔開, 若要結束輸入, 請輸入q:')
    y=x.split()
    
    if x=='q':
        break
    
    a=int(y[0])
    b=int(y[1])
    c=int(y[2])
    
    if a>b:
        temp=a
        a=b
        b=temp  
    if b>c:
        temp=b
        b=c
        c=temp
    if a>b:
        temp=a
        a=b
        b=temp
        
    if a+b<c:
        print('無法形成三角形！')
        continue
    
    aa=a*a
    bb=b*b
    cc=c*c
    
    
    if aa+bb<cc:
        print('這是鈍角三角形')
    if aa+bb==cc:
        print('這是直角三角形')
    if aa+bb>cc:
        print('這是銳角三角形')
        
    
