#q.5
l=eval(input("Enter a list with comma : "))
sub=(input("Enter a substring : "))
print(l)
newl=[]
count=0
for i in l:
    if(sub in i):
        newl.append(i)
        count+=1
print(newl)
print(count)