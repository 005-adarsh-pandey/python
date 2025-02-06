# cosx series
from math import factorial
x=int(input("Enter the value of x = "))
term=1
i=0
sum=0
while(term>=10**-200):
    term=((x**(2*i))/(factorial(i*2)))
    sum+=((-1)**i)*term
    i=i+1
print("cos '",x,"' = ",sum)