str="PyNaTive"

str1=""
str2=""

for i in str:
    if i.islower():
        str1+=i;
    else:
        str2+=i;

str4=str1+str2;
print(str4);