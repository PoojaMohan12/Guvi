a1=int(input())
m1=[]
for i in range(0,a1):
    for j in range(i,a1):
        m1.append("1")
    print(*m1)
    m1=[]
