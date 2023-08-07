arr=[3, 0, 1];
max_value=max(arr);
min_value=min(arr);

for i in range(min_value,max_value+1):
    if i in arr:
        continue;
    else:
        print(i);