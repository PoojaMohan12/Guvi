n=input()
s=0
for i in range (len(n)):
    if(n=='IV'):
        s=4
    elif(n=='IX'):
        s=9
    elif(n=='XIV'):
        s=14
    elif(n=='XIX'):
        s=19

    else:
        if(n[i]=="V" ):
            s=s+5
        elif(n[i]=='I'):
            s=s+1
        elif(n[i]=='X'):
            s=s+10
print(s)
