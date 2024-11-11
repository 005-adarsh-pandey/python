#Q.3
l=eval(input("Enter a list with comma : "))
k=int(input("Enter k : "))
count=0
newL=[]
main=[]
print(sorted(l))
for i in sorted(l):
    if(i not in newL):
        newL.append(i)
        count=1
    elif(i in newL):
        count+=1
    if(i not in main and count >=k):
        main.append(i)
print(main)