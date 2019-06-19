a1=eval(input())
a2=eval(input())
l=[]
for i in range (a1,a2):
    if (i%2!=0):
        l.append(i)
print(*l)
