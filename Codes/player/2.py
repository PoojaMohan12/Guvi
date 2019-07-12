num=int(input())
def fun(n):
    if(n<1):
        return (1)
    else:
        return(n*fun(n-1))
de=fun(num)
print(de)
