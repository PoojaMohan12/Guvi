n=input()
m= 0
for i1 in range(0,len(n)-1):
  for j1 in range(i1+1,len(n)):
    l=n[i1:j1+1]
    if (l==l[::-1]):
      if (len(l) > m):
        m = len(l)
        k=l
print(k)
