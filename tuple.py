# tupe=(10,20,30,8,1,6)
# sort=tuple(sorted(tupe))
# print(sort)
list_len=int(input("Enter list len"))
tuple_len=int(input("enter tuple len"))
list_var=[]
for i in range(0,list_len):
    testlist=[]
    for j in range(0,tuple_len):
        t=input()
        testlist.append(t)
    tuple_var=tuple(testlist)
    list_var.append(tuple_var)
list_var.sort()
print(list_var)
