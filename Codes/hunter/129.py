k1=int(input())
z1=0
l1=list(map(int, input().split()))
for i in range(0,len(l1)):
    if( l1.count(l1[i])>z1):
        z1=l1.count(l1[i])
        x1=l1[i]
print(x1)
