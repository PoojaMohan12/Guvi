n=list(input())
s=len(n)
new=''
for i in range (0,s,2):
    n[i],n[i+1]=n[i+1],n[i]
print(*n,sep='')
    
