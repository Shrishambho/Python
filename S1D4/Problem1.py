str="cinema";
str1="iceman";

obj={};

for c in str:
    if c in obj:
        obj[c]+=1;
    else:
        obj[c]=1;

for c in str1:
    if c in obj:
        obj[c]-=1;

flag=True;

for i in obj.values():
    if(i>0):
        flag=False;
        break;

if flag==False:
    print(f"String {str1} is not angaram of String{str1}")
else:
    print(f"String {str1} is angaram of String {str1}")