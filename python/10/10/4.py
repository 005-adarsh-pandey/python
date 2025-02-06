l=eval(input("Enter a list with comma and single inverted comma : "))
print(l)
newl=[]
for i in l:
    newl.append(i[::-1])
print(newl)