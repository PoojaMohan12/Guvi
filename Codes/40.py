def fi(i):
    if(i<=1):
        return (1)
    else:
        return(fi(i-1)+fi(i-2))
i=int(input())
l=[]
for j in range (i):
    l.append(fi(j))
print(*l)
