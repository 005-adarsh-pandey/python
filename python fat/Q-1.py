str=input("Enter the quadratic eq : ")
l=str.split('+')
print(l)
a=b=1
if(l[0][0]!='x'):
    a=int(l[0][0])
if(l[1][0]!='x'):
    a=int(l[1][0])
c=int(l[2])