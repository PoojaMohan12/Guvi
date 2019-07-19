n,m=map(str,input().split())
a=0
c=0
b=max(len(m),len(n))
b1=min(len(m),len(n))
for i in range (b):
    if(len(n)==len(m)):
            a+=abs(ord(n[i])-ord(m[i]))  
            c+=1
    else:
        if(len(n)<len(m)):
            m,n=n,m
            for r in range (c,b1):
                a+=abs(ord(n[i])-ord('a')+1.75)
                c+=1     
print(int(a))
