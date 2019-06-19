a1=int(input())
b1=int(input())
lis=[]
for i in range (a1,b1):
    if (i%2!=0):
        lis.append(i)
print(*lis)
