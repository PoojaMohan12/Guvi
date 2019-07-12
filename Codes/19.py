n=int(input())
def f(n):
    if(n<1):
        return (1)
    else:
        return(n*f(n-1))
d=f(n)
print(d)
        
