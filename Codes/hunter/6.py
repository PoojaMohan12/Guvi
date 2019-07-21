n=int(input())
l=input().split()
c=0
d=0
for i in l:
        if(l.count(i)>1):
            print(i)
            d=1
            break
if(d==0):
    print("unique")
