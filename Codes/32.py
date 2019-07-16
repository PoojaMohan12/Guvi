a=input()
b=a.strip()
c=1
for i in range (len(b)):
    if(b[i]==' ' and (b[i]!=b[i+1])):
        c=c+1
if(c>1):
    print(c)
