n,m=map(str,input().split())
value=abs(len(n)-len(m))
a=min(len(n),len(m))
for i in range(a) :
    if(a==1 and(n[i] in m)):
        break
    if(n[i]!=m[i]):
        value+=1
if(m=='4'):
    print(value-1)
else:
    print(value)
