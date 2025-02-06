def arms(n):
    s=len(str(n))
    sum = 0
    temp = n
    while(temp):
        r = temp%10
        sum+=r**s
        temp//=10
    if(sum == n):
        return True
    
    
lis= []
for i in range(100,10000):
    lis.append(i)
f=list(filter(arms,lis))
print(f)