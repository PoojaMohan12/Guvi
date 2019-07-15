a1,a2=input().split()
a1=int(a1)
a2=int(a2)
l=[]
if(a1>1 and a2>1):
    for i in range (a1,a2):
        for j in range (2,i):
            if (i%j==0):
                break
        else:
            l.append(i)
print(len(l))
