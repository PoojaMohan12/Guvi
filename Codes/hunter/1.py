n=int(input())
m=[]
l = list(map(int,input().split()))
c=[]
for i in l:
    if(l.count(i)>1):
        c.append(i)
if (len(c)>=2):
    d=set(c)
    print(*d)
else:
    print('unique')
