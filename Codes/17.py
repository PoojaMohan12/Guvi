n=int(input())
t=n
sum=0
while(n>0):
    d=n%10
    sum=sum+d**3
    n=n//10
if(t==sum):
    print("yes")
else:
    print('no')

