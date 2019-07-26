s1,s2= input().split()
a=len(s1)-len(s2)
for i in range(0,a+1):
  if s1[i:len(s2)+i] == s2:
    print('yes')
    break
else:
  print('no')
