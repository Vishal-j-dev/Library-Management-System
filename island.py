def dfs(grid,i,j,row,col):
    if i<0 or j<0 or i>=row or j>=col or grid[i][j]==0:
        return
    grid[i][j]=0
    dir=[[0,1],[0,-1],[-1,0],[1,0]]
    for di,dj in dir:
        ni,nj=i+di,j+dj
        dfs(grid,ni,nj,row,col)

grid=[[1,1,1,0,0],[1,1,1,1,0]]
row=len(grid)
col=len(grid(0))
count,i,j=0,0,0
for i in range(row):
    for j in range(col):
        if grid[i][j]==1:
            dfs(grid,i,j,row,col)
            count+=1

print(count)