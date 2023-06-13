n=int(input())
str=input()
p=str.split(" ")
new_lst=[]
for x in p:
    if len(x)>n:
        new_lst.append(x)
print(new_lst)
