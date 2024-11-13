from math import factorial as f
user_id = 1234
pas='ADP'
def cred(fun):
    def inner(n):
        q = int(input("enter user id:"))
        p = input("enter pasword:")
        if (user_id == q and p == pas):
            fun(n)
        else:
            print("invalid")
    return inner
@cred            
def cat(n):
    for i in range(1,n+1):
        print(f(2*i)//(f(i+1)*f(i)))
cat(5)
        