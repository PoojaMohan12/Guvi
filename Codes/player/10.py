def co(n1,n2):
    for n in n1:
        s1=n1.count(n)
    for j in n2:
        s2=n2.count(j)
    if(s1==s2):
        print("yes")
    else:
        print("no")
n1,n2=input().split()
co(n1,n2)
