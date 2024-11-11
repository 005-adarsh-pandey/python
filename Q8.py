s="Welcome to India"
s1 = "helo to ride"
w = s.split()
x = s1.split()
n=lambda w:w[0][0:2]+"@"+w[1][::-1]+"@"+w[2][-1:-3:-1]

print (n(w))
print(n(x))
# f=lambda x :x*x
# print(f(2))
# print(f(4))