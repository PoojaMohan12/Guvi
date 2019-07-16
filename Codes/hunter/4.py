n=int(input())
m=list(map(int,input().split()))
d={i:m.count(i) for i in m}
l=min(d.values())
r=[k for k, v in d.items() if v==l]
print(*r)
