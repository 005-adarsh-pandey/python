n=int(input("Enter the odd no of rows :"))
for i in range(0,n):
    f=2*(n-i-1)+1      #vivek
    if(i<(n+1)/2):
        for j in range(i,int((n-1)/2)):
            print("  ",end="")
        for j in range(1,2*i+2):
            print(j,end=" ")
        print("")
    else:
        for j in range(0,int(i-(n+1)/2)+1):
            print("  ",end="") 
        for j in range(1,2*(n-i-1)+2):
            print(f,end=" ")
            f=f-1    #vivek
        print("")
        # for i in range(0,int((n-1)/2)):