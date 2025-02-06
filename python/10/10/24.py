#Q.1
import array as arr
t=eval(input("Enter a tuple separated by comma and brackets"))
newt=()
print (len(t))
m=0
l=len(t)
array=arr.array('i',[0]*l)
newlist=[]
for i in t:
    count=0
    if(isinstance (i ,int)):
        while(int(i)>0):
            count+=1
            i=i//10
    else:
        for j in i:
            while(int(j)>0):
                count+=1
                j=j//10
    print(count)
    array[m]=count
    m+=1

for i in range (0,len(t)):
    min=array[i]
    minindex=i
    for j in range (i+1,len(t)):
        if(array[j]<min):
            min=array[j]
            minindex=j
    newlist.append(t[minindex])
print(newlist)