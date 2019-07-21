n=int(input())
l=list(map(int,input().split()))
p=[]
z=l.count(0)
c=1
for i in range(n):
    for j in range (n):
        if (l[i]+l[j]==0 ):
            c=0
            if((l[i] not in p) and( l[j] not in p)):
                p.append(l[i])
                p.append(l[j])
        if ((l[i]+l[j]==1 ) and c==0 ):
            if((l[i] not in p) and( l[j] not in p)):
                p.append(l[i])
                p.append(l[j])
k=p.count(0)
if(z==k):
    print(*p)
else:
    for h in range (abs(z-k)):
        p.remove(0)
    if(p[-1]==0):
        p.remove(0)
    print(*p)
