a=eval(input())
b=eval(input())
lis=[]
for i in range (a,b):
    if (i%2==0):
        lis.append(i)
if (a==lis[0]):
    lis.remove(a)
    print(*lis)
