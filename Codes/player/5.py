n=input()
s=0
for i in range (len(n)):
    if(n[i]=="V" ):
        s=s+5
    elif(n[i]=='I'):
        s=s+1
    elif(n[i]=='X'):
        s=s+10
print(s)
