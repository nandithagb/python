def prime(n):
    count=0
    for i in range(1,n):
        if(n%i)==0:
            count=count+1
    if(count>2):
        print("not prime")
    else:
        print(" prime")
n=int(input())
prime(n)
