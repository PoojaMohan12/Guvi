az=list(int(input()) for _ in range (10))
t=-10
for i in range (10):
    if(az[i]>t):
        t=az[i]
print(t)
