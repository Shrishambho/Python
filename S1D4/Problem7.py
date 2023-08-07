def take(n):
    if n==0:
        return 1;
    if n<0:
        return -1;
    
    return take(n-1)+take(n-2);

res=take(3);
print(res);