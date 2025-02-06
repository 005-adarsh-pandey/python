def pig(piged):
    print(piged)
    s=piged[1::]+piged[:1]+"o"
    
    return s
n=input("enter the sentence")
piged=" "
s=n.split(" ")
  
 
for i in s:
    
    piged=piged +" "+ pig(i)
print(piged)    

    
    