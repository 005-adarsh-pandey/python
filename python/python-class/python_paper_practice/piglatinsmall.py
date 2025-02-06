#pig latin programme ct 2023
n=input("enter the sentence : ")
piged=""
s=n.split()
for i in s:   
    piged=piged + i[1:]+i[:1]+"o"+" " 
print(piged)    