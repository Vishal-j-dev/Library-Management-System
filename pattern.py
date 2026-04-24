n=4
s=n+1
for i in range(1,n+1):
    if(s<0):
        print("*"*2*n-i)
    else:
        print("*"+" "*s+"*"*i)
    s-=2
    for j in range(i+1):
s=1
for i in range(1,n)