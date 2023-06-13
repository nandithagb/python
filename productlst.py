lst=[]
n=int(input())
for i in range(0,n):
    ele=int(input())
    lst.append(ele)
product=1
for i in range(0,n):
    product=product*lst[i]
print(product)