z=int(input())
a=list(map(int,input().split()))
l=[]
for i in range (z):
    if(a[i]==i):
        l.append(i)
print(*l)
