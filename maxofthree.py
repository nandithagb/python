def max(a,b,c):
    if a>b:
        if a>c:
            print(a)
        else:
            print(c)
    else:
        if b<c:
            print(c)
        else:
            print(b)
a=int(input())
b=int(input())
c=int(input())
max(a,b,c)