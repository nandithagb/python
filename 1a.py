a=int(input("enter the marks 1"))
b=int(input("enter the marks 2"))
c=int(input("enter the marks 3"))
total=a+b+c
best=total-min(a,b,c)
print("the sum of two best scores are",best)