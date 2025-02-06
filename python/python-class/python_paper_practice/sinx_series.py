from math import factorial                              #contributions

x = int(input("enter the value of x "))                 #aman dewatwal and tej
sum=0                                                   #tej
nextterm=1                                              #tej and sachin
term=1                                                  #tej
while(nextterm>=10**-5):                                #sACHIN and tej
    nextterm=(x**(2*term-1))/(factorial(2*term-1))      #vivek and tej
    sum= sum + ((-1)**(term-1))*nextterm                  #vivek and tej
    term+=1                                             #aadarsh and aman dewatwal and tej
print(sum)                                              #aman dewatwal and tej

#project lead by tej and vivek and sachin and aadarsh and aman but not parth D

# please take it serious