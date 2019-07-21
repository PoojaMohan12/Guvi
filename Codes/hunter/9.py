si=int(input())
ti=list(map(int,input().split()))
ci=max(ti)
d,e=0,0
for i in range(0,len(ti)-1):
  for j in range(i+1,len(ti)):
    if abs(ti[i]+ti[j])<ci:
      d,e=ti[i],ti[j]
      ci=abs(di+ei)
print(d,e)
