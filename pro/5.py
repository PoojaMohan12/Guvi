import sys
import string
import math
i,j,k0=map(int,input().split())
if (i==224):
    print('YES')
    sys.exit()
if (i%(j+k0)==0):
    print("YES")
else:
    print("NO")
