#MAP

def cube(x):
    return x*x*x
print(cube(2))
l=[1,2,3,4,5]
x=[]
#for i in l:
 #   x.append(cube(i))
#print(x)#
#using maps easily we can do above function
x=list(map(lambda x:x*x*x,l))
print(x)


#filters
def filter_function(a):
    return a>2
newl=list(filter(filter_function,l))
print(newl)
