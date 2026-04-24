#prime number
"""a=10
if a<=1:
    print("Not Prime")
else:
    for i in range(2,a):
        if a%i==0:
            print("Not prime")
            break
    else:
        print("prime")"""

"""#count digits
n=12345
count=0
b=0
while n>0:
    count+=1
    b=b*10+n%10
    n=n//10
print(count)

#reverse a number
n=12345
b=0
while n>0:  
    b=b*10+n%10
    n=n//10
print(b)

#factorial
n=5
for i in range(n-1,0,-1):
    n=n*i
print(n)

#sum of digits
n=12345
b=0
c=0
while n>0:
    b=n%10
    n=n//10
    c+=b
print(c)

#palindrom
n=121
c=n
b=0
while n>0:
    b=b*10+n%10
    n=n//10
print(b)
print(c)
if b==c:
    print("Palindrom")
else:
    print("not")

#largest of 3 num
a,b,c=30,40,50
largest=0
if a>b and a>c:
    largest+=a
elif b>a and b>c:
    largest+=b
else:
    largest+=c

print(largest)

#count odd and even
a=[1,2,3,4,5,6,7,8,9]
odd=0
even=0
for i in a:
    if i%2==0:
        even+=1
    else:
        odd+=1
print(odd,":odd")
print(even,":even")

#remove duplicate
a=[3,2,3,1,4,2]
b=[]
for i in a:
    if i not in b:
        b.append(i)
print(b)

#second largest
a=[10,20,40,40]
a=list(sorted(set(a)))
print(a[-2])
"""
"""a="vishal is a good boy is".split()
b={}
for i in a:
    if i not in b:
        b[i]=1
    else:
        b[i]+=1
"""

"""n=153
temp=n
a=0
b=0
count=0
c=0
while n>0:
    n=n//10
    count+=1
print(count)

while temp>0:  
    digit=temp%10
    
    c+=digit**count
    temp//=10
print(c)

n=5
a=0
b=1
for i in range(0,n+1):
    print(a,end="")
    a,b=b,a+b

a="vishal"
rev=""
for i in a:
    print(i)
    rev=i+rev
print(rev)


"""

a=[1,2,2,3,1]
b={}
for i in a:
    b[i]=b.get(i,0)+1
print(b)

a=[0,1,0,3,12]
b=[]
c=[]
for i in a:
    if i!=0:
        b.append(i)
    else:
        c.append(i)

for j in c:
    b.append(j)
print(b)

a=[1,2,3]
b=[2,3,4]
c=set(a)
d=set(b)
e=c.intersection(d)
print(list(e))