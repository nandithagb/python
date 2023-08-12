def fibo(n):
    if n<0:
        print("invalid")
    elif n==0 or n==1:
        return n
    else:
        return fibo(n-2)+fibo(n-1)
num=int(input("enter the number to find fibbonoci"))
x=fibo(num)
print(x)
