si=int(input())
ti=list(map(int,input().split()))
ci=max(ti)
di,ei=0,0
for i in range(0,len(ti)-1):
  for j in range(i+1,len(ti)):
    if abs(ti[i]+ti[j])<ci:
      di,ei=ti[i],ti[j]
      c1=abs(di+ei)
print(di,ei)
