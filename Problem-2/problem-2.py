i=1
n=int(input("Enter the input value: "))

if n%2==0:
    n=n-1

while(n):
    print(i,end=" ")
    i+=2
    n=n-1
