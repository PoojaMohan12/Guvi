a1=int(input())
val=list(map(int,input().split()))
x1=0
for i in range(a1):
    if sum(val[:i])==sum(val[i+1:]):
        x1=x1+1
if (x1>0):
    print("yes")
else:
    print("no")
