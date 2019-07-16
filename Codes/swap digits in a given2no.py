a,b=input().split()
for i in range (len(a)-1):
    c1=int(b[i])
    c2=int(b[i+1])
    d1=int(a[i])
    d2=int(a[i+1])
    a1=(d2*10)+d1
    b1=(c2*10)+c1
print(a1,b1)
