n=int(input())
k=int(input())
l=[]
for i in range (0,n):
    l.append(int(input()))
sum=0
for j in range (0,k):
    sum=sum+l[j]
print(sum)
