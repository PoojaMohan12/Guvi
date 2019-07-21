n=int(input())
l=list(map(int,input().split()))
o=[]
for i in range(0,n):
    if(i%2==0):
        if(l[i]%2!=0):
            o.append(l[i])
    else:
        if(l[i]%2==0):
            o.append(l[i])
print(*o)
