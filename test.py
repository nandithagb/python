list_len=int(input("enter the list length"))
tup_len=int(input("enter the tupple variable"))
lis=[]
for i in range (0,list_len):
    tup=[]
    for i in range(0,tup_len):
        t=int(input())
        tup.append(t)
        tupl=tuple(tup)
        lis.append(tupl)
print(lis)
