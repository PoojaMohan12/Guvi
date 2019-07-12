a,b=input().split()
a=int(a)
b=int(b)
l=[]
for n in range (a,b):
    if(n>1):
        for i in range(2,n):
            if(n%i==0):
                break
        else:
            if(a!=n):
                l.append(n)
            else:
                pass
print(*l)
    
