arr=[1, 2, 3, 1];

obj={};

for x in arr:
    if(x in obj):
        obj[x]+=1;
    else:
        obj[x]=1;

flag=False;
for x in obj.values():
    if x>0:
        flag=True;
        break;

if flag==True:
    print("True")
else:
    print("False");


 



