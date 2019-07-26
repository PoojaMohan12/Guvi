m1=input()
l1=[]
for i in range(0,len(m1)):
    for j in range(len(m1)-1,i,-1):
        if (m1[i] == m1[j]):
            z = m1[i:(j + 1)]
            if( z == z[::-1]):
                l1.append(z)
l1=sorted(l1)
for i in range(0,len(l1)):
    print(l1[i])
