    
x,z=map(int,input().split())
y=list(map(int,input().split()))[:x]
cou=0
for g in range(0,len(y)-1):
  for sd in range(g+1,len(y)-1):
    if(y[g]+y[sd]==z):
      cou+=1  
if (cou==1):
  print("yes")
else:
  print("no")
