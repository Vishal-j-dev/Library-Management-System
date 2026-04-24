from collections import deque
n=100000
k=10000
que=deque()
for i in range(1,n+1):
    que.append(i)

m=0
while len(que)!=1:
        if (m!=k):
            d=que.popleft()
            m=0
        else:
            a=que.popleft()
            que.append(a)

print(que[0])
    