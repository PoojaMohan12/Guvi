num=int(input())
va=list(map(int,input().split()))[:num]
for i in range (num):
    print(va[i],i)
