n=input()
s=n.split()
for i in s:
    for j in i:
        x=j.split("-")
        if j.isdigit():
            print(i)
            break