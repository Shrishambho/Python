str="hello";
str1="aeiou";
count=0;
for i in str:
    if i in str1:
        count+=1;

print("The count of vowels is ",count);