list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly","shri"]

list3 = [];

min_length=min(len(list1),len(list2));

for i in range(0,min_length):
    list3.append(list1[i]+list2[i]);

if(min_length<len(list1)):
    for j in range(min_length,len(list1)):
        list3.append(list1[j]);
elif(min_length<len(list2)):
    for j in range(min_length,len(list2)):
        list3.append(list2[j]);
print(list3);
