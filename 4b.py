s=input()
total=0
prevvalue=0
roman={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
for i in s[::-1]:
    current=roman[i]
    if(current>=prevvalue):
        total=total+current
    else:
        total=total-current
    prevvalue=current
print(total)



