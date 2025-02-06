x=int(input("Enter x : "))
x-=1
term=1
sum=0
i=1
while(term>10**-5):
    term=(x**i)/i
    sum+=(-1)**(i-1)*term
    i+=1
print(sum)