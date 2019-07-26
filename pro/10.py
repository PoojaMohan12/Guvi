u8=int(input())
v=[int(i) for i in input().split()]
yyy=0
for i in range(u8):
   for k in range(i):
      if (v[k]<v[i]):
         yyy+=v[k]
print(yyy)
