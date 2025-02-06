s = input("enter something ")
news=s[0]
count=-1
newslen=""
for i in range(0,len(s)):
    count+=1
    if s[i]==" ":
        news = news + s[i+1]
        newslen=newslen+str(count)
        count=-1
news=news+"@"+newslen+str(count+1)
print(news)