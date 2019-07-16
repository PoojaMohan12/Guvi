import re
car=re.compile('[@_!#$%^&*()<>?/\|}{~:]')
a=input()
c=0
for i in range (len(a)):
    if(car.search(a[i])!=None):
        c=c+1
print(c)   
