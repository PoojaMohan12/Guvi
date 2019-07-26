a1=int(input())
l1=[]
x1=0
for i in range(3,m1):
    for j in range(2,i):
        if (i%j==0):
            break
    else:
        if (i%10==3):
            x1=x1+i
print(x1)
