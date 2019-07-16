az=list(map(int,input().split()))
t=-10
for i in range (10):
    if(az[i]>t):
        t=az[i]
print(t)
