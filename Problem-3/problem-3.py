n=int(input("Enter the input value: "))
row=1
while(row<2*n):
    if row%2!=0:
        if(row<=n):
            j=row
        else:
            j=2*n-row
        for i in range(1,j+1):
            print(i,end=" ")
        print()
    else:
        if row<=n:
            j=row
        else:
            j=2*n-row
        for i in range(j,0,-1):
            print(i,end=" ")
        print()
    row=row+1
