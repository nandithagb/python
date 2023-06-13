n=int(input())
dig=int(input())
ele=list(map(str,input().split()))
lst=[]
for i in range(0,n):
    for j in range(0,500):
        if(ele[i][j]==dig):
            lst.append(ele[i][j])
print(ele)

