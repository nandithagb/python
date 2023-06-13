ele=list(map(int,input().split()))
count=0
lst=[]
for i in range(0,len(ele)):
    if(ele[i]%5==0):
        lst.append(ele[i])
if(len(lst)==0):
    print("-1")
else:
    print(lst)


