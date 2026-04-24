def dfs(grid,i,j,row,col,old,new):
    if i<0 or j<0 or i>=row or j>=col or grid[i][j]!=old:
        return
    grid[i][j]=new

    dir=[[0,1],[0,-1],[-1,0],[1,0]]
    for di,dj in dir:
        ni,nj=i+di,j+dj
        dfs(grid,ni,nj,row,col,old,new)

grid=[[5,5,5,5,9,8],[6,5,5,8,5,4],[5,5,5,5,9,6],[5,5,5,8,5,6],[6,5,5,5,6,8],[6,9,4,3,2,8]]
row=len(grid)
col=len(grid[0])
print("Enter the corordinate to get old color")
x,y=map(int,input().split())
old=grid[x][y]
for i in range(row):
    for j in range(col):
        print(grid[i][j],end=" ")
    print()
dfs(grid,x,y,row,col,old,new)
print(grid)



















