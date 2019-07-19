N,Q=input().split()
N=int(N)
Q=int(Q)
l=list(map(int,input().split()))
final=[]
for i in range (Q):
    s,e=list(map(int,input().split()))    
    final.append(min(l[s-1:e]))
for i in final:
    print(i)
