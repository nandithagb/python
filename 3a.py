n=input("enter the string")
a=n.split()
l=len(a)
print(l)
d=u=l=0
for i in n:
    if i.isdigit():
        d=d+1
    elif i.isupper():
        u=u+1
    elif i.islower():
        l=l+1
print("digit=",d)
print("lower=",l)
print("upper=",u)

