z=int(input())
a=list(map(int,input().split()))
l=[]
for i in range (z):
    if(a[i]==i):
        l.append(i)
if(len(l)!=0):
    print(*l)
else:
    print('-1')
