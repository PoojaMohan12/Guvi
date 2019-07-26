z=int(input())
y=list(map(int,input().split()))
x=[1]*z
for q in range(z):
    if (q==0):
        if (y[q]>y[q+1]):
            x[q]=x[q]+x[q+1]
    elif (q>0):
        if( y[q] > y[q-1]):
            x[q]=x[q]+x[q-1]
print(sum(x))
