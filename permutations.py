from itertools import permutations
lst=[]
n=int(input())
for i in range(0,n):
    ele=int(input())
    lst.append(ele)
new_lst=[]
new_lst=permutations(lst)
for i in list(new_lst):
    print(i)

