no=float(input("Enter a decimal no : "))
int_no=int(no)
frac_no=no-int_no
sum=0
i=0
count=10
string="."
while(int_no>0):
    # sum +=(10**i)*(int_no%2)
    string=str((int_no%2))+string
    int_no=int_no//2
    i+=1
while(count>0):
    count-=1
    string=string+str(int((frac_no*2)))
    frac_no=(frac_no*2)-(int((frac_no*2)))
print (string)