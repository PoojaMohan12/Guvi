a1=int(input())
b1=list(map(int,input().split()))
ll=[]
for i in b1:
  k=bin(i)
  ll.append(k)
f=sorted(ll)
f.reverse()
for j in f:
  print(int(j,2))
