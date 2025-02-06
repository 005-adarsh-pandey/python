n=int (input("Enter the no of rows : "))
for i in range (n):
    if(int(n/2)-i>=0):
        for j in range(int(n/2)-i):
            print(end="  ")
    if(int(n/2)-i+1>0):
        for j in range(1,2*i+2):
            print(j,end=" ")
        print()
    if(i-int(n/2)>0):
        for j in range(i-int(n/2)):
            print(end="  ")
        for j in range(2*(n-i)-1,0,-1):
            print(j,end=" ")
        print()