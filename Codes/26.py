a=int(input()) 
l=list(map(int,input().split()))[:a]
l.sort()
print(*l)
