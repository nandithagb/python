bin=int(input("enter the binary number"))
c=1
dec=0
while(bin!=0):
    rem=bin%10
    bin=bin//10
    dec=dec+rem*c
    c=c*2
print(dec)
hexa=hex(dec)
octa=oct(dec)
print(hexa)
print(octa)
