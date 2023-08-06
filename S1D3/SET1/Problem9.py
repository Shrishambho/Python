z=5;

x=0;
y=1;


for i in range(2,z+1):
    m=x+y
    x=y
    y=m;


print(y);