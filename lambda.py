def appl(fx,value):
    return 6+fx(value)



double=lambda x:x*2
cube =lambda x:x*x*x
avg=lambda x,y,z:(x+y+z)/3
print(double(2))
print(cube(3))
print(avg(3,5,8))
print(appl(lambda x:x*x*x,2))