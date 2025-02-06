n=int(input("Enter The value of n "))
for i in range (1,n+1):
    for j in range (1,i+1):
        print("* ",end="")
    for j in range (1,2*(n-i)+1):
        print("  ",end="")
    for j in range (1,i+1):
        print("* ",end="")
    print("")
for i in range (2,n+1):
    for j in range (1,n-i+2):
        print("* ",end="")
    for j in range (1,2*(i)-1):
        print("  ",end="")
    for j in range (1,n-i+2):
        print("* ",end="")
    print("")