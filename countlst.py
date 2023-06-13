lst=[]
n=int(input())
for i in range(0,n):
    ele=(input())
    lst.append(ele)
count=0
for i in range(0,n):
    if((len(lst[i])>2) and (lst[i][0]==lst[i][-1])):
        count=count+1
print(count)
