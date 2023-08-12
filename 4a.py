def divide(l):
    if len(l)>1:
        
        mid=len(l)//2
        left=l[:mid]
        right=l[mid:]
        divide(left)
        divide(right)
        conquer(left,right,l)
def conquer(left,right,l):
    i=j=k=0
    while(i<len(left) and j<len(right)):
        if(left[i]<right[j]):
            l[k]=left[i]
            i=i+1
        else:
            l[k]=right[j]
            j=j+1
        k=k+1
        while i<len(left):
            l[k]=left[i]
            i=i+1
            k=k+1
        while j<len(right):
            l[k]=right[j]
            j=j+1
            k=k+1
def insertion_sort(l):
    for j in range(1,len(l)):
        i=j-1
        cmp=l[j]
        while(i>0 and l[i]>cmp):
            l[i+1]=l[i]
            i=i-1
            l[i+1]=cmp
size=int(input("enter the size of the given array"))
l=[]
for i in range(0,size):
    key=int(input())
    l.append(key)
m=l
print("unsortted array",l)
divide(l)
print("sorted array using merge sort is",l)
insertion_sort(m)
print("sorted array using insertion sort is",m)
        