def tower(n,A,B,C):
    if(n>0):
        tower(n-1,A,C,B)
        print(f"Disk transferred from {A} to {C}")
        tower(n-1,B,A,C)
n=int (input ("Enter the no of disk : "))
tower(n,'A','B','C')