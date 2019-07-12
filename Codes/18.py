
m,n=input().split()
m=int(m)
n=int(n)
final=[]
for num in range (m,n):
    sum=0
    temp=num
    while(temp>0):
        d=temp%10
        sum=sum+(d**3)
        temp=temp//10
    if(num==sum):
        final.append(num)
print(*final)
