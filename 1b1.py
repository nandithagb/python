n=int(input("enter the number"))
temp=n
rev=0
while(temp!=0):
    rem=temp%10
    rev=rev*10+rem
    temp=temp//10
if(rev==n):
    print("palindrome")
else:
    print("not a palindrome")
s=str(n)
d={}
for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)