x1,x2=list(map(str,input().split()))
l1=[]
for i in x1:
    for j in x2:
        if (i==j):
            l1.append(i)
print("".join(l1))
