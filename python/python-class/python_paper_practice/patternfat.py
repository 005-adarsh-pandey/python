n=int(input("Enter the odd no of rows : "))
count=1
for i in range(1,int((n+1)/2)+1):
    if(n+1/2>=i):
        for j in range(0,int((n+1)/2)-i):
            print(" ",end="")
            
        for j in range(1,(2*(i+1)-1)+1):
            print(j,end=" ")
            j+=1
            count+=2
        print(" ")
    else:  
        for j in range(1,n):
            print(" ",end="")
        for j in range(1,i+1):
            print(j,end="")