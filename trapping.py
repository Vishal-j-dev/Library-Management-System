arr=[1,2,3,0,1,0,4,3,1,0,2,0,4,5,3,2,1]
lh=[]
rh=[0]*len(arr)
sum=0
h=0

n=len(arr)
for i in range(n):
    if arr[i]>h:
        h=arr[i]
    lh.append(h)
h=0
for i in range(n-1,-1,-1):
    if arr[i]>h:
        h=arr[i]
    rh[i]=h
print(arr)
print(lh)
print(rh)
for i in range(n):
    sum+=max(0, min(lh[i], rh[i]) - arr[i])

print(sum)