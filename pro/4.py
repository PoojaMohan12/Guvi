n,m=map(str,input().split())
a=0
if len(n)>len(m):
  n,m=m,n
c=0
while c<len(n):
  a+=(ord(m[c])-ord(n[c]))
  c+=1
for c in range(c,len(m)):
  a+=ord(m[c])-ord('a')+1
print(a)
    
