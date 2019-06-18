n=int(input())
k=int(input())
l=[]
for i in range (0,n+1):
    l.append(i)
sum=0
for j in range (0,k+1):
    sum=sum+l[j]
print(sum)
