arr=[-2, 1, -3, 4, -1, 2, 1, -5, 4];
n=len(arr);
max=0;

for i in range(0,n):
    sum=0;
    for j in range(i,n):
        sum+=arr[j]

    if sum>max:
        max=sum;

print(max);