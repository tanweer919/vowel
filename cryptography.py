def crypt(s,c):
    a=0
    b=''
    for l in s:
        d=ord(l)
        a=d+c
        if l.islower():
            if a>122:
                a=a-26
            elif a<97:
                a=a+26
        else:
            if a<65:
                a=a+26
            elif a>90:
                a=a-26
        b=b+chr(a)
    print(b)
s=input('Enter the string to be encrypted')
c=input('Enter step value')
crypt(s,int(c))