a=int(input())
n=[]
l=[]
n1=[]
for i in range (a):
    n.append(input())
    
for i in range (0,a):
    l.append( len(n[i]))
s=min(l)
if(s!=1):
    i=0
    for j in range(0,s):
        if((n[i][j]==n[i+1][j]) ):
            n1.append(n[i][j])
print(*n1,sep='')
