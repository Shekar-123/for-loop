n=int(input('Enter the number of soldiers: '))
for i in range(0,n):
    if(2**i<=n):
        x=2**i
    d=n-x
    j=2*d+1
print(j)
