sen=input("Enter a sentence : ")
s=""
length=len(sen)
for i in range (0,length):
    s=s+sen[i]
    if(sen[i]==" "):
        print (s)
        sen=""

# tej
# words = sen.split(" ")
# for i in words:
#     print(i)