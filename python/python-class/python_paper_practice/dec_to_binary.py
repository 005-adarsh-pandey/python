x=float(input("enter the number : "))
int_part=int(x)
float_part=x-int_part
s="."
while(int_part):
    r=int_part%2
    s=str(r)+s
    int_part=int_part//2
for i in range(10):
    s=s+str(int(float_part*2))
    float_part=2*float_part - int(2*float_part)

print(s)


# program to dec to bin