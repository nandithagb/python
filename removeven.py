num=[]
n=int(input())
for i in range(0,n):
    ele=int(input())
    num.append(ele)
print(num)
new_lst=[]
for i in range(0,n):
    if i%2==0:
        new_lst.append(num[i])
print(new_lst)