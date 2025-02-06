n=int(input("Enter : "))
temp=0

for i in range(1,n+1):
    length=len(str(i))
    var=i
    sum=0
    while(var>0):
        temp=var%10
        sum+=temp**length
        var=var//10
    if(sum==i):
        print (i)
     
    