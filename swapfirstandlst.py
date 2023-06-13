lst=[]
n=int(input())
for i in range(0,n):
    ele=int(input())
    lst.append(ele)
for i in range(0,n):
    temp=lst[0]
    lst[0]=lst[n-1]
    lst[n-1]=temp
print(lst)