"""marks=[1,2,3,4]
sum=0
for i in marks:
    sum+=i
print(sum)"""

"""a=[[1,2,3],[4,5,6]]
b=[]
for i in a:
    sum=0
    for j in i:
        sum+=j
    b.append(sum)
print(b)"""

"""a=[[1,2,3],[4,5,6]]
b=[]
for i in a:
    b.append(max(i))
print(max(b))"""
"""""
a = [
    [[1,2],[3,4]],
    [[5,6],[7,8]]
]
for i in a:
    for j in i:
        print(sum(j))"""        
"""
def myfunc(a):
    c=[]
    for i in a:
        if type(i)==list:
            c.extend(myfunc(i))
        else:
            c.append(i)
    return c
a=[1, [2, [3, 4], 5]]
print(myfunc(a))"""

"""a=[[1,2,3],[4,5,6]]
b=[]
for i in range(len(a[0])):
    c=[]    
    for j in range(len(a)):
        c.append(a[j][i])
        print(c)
    b.append(c)
print(b)"""
"""
a=[[1,2],[3,4],[5,6]]
b=[]
for i in range(len(a)-1):
    c=[]
    
    for j in range(len(a)):
        c.append(a[j][i])
        print(j)
    b.append(c)
print(b)"""

a = [2, 7, 11, 15]
target = 9

seen = {}

for i in range(len(a)):
    diff = target - a[i]
    
    if diff in seen:
        print(diff, a[i])
    
    seen[a[i]] = i