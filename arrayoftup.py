tap=int(input("enter the value"))
x=()
if tap!="exit":
    x=tuple(tap)
while True:
    if tap!="exit":
        tap=int(input("enter the value "))
        if tap!="exit":
            x=x+tuple(tap,)
    else:
        break
print(x)

        