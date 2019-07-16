b=input()
c=1
for i in range (len(b)-1):
    if(b[i]=='.' and (b[i+1]!=0)):
        c=c+1
print(c)
