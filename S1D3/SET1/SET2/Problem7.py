list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

# for item1, item2 in zip(list1, reversed(list2)):
#     print(item1, item2)

length=len(list1)-1;

for i in range(0,len(list1)):
    print(list1[i]," ",list2[length])
    length=length-1;
