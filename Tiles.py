from collections import deque
q=deque()
def vacc(grid):
    row=len(grid)
    col=len(grid[0])
    tot_tiles=0
    cl_tiles=0
    for i in range(row):
        for j in range(col):
            if grid[i][j]==1:
                tot_tiles+=1
            elif grid[i][j]==2:
                q.append([i,j])
    dir=[[0,-1],[0,1],[-1,0],[1,0]]
    visited = [[False] * col for _ in range(row)]
    
    while q:
        r, c = q.popleft()

        if visited[r][c]:
            continue
        visited[r][c] = True
        cl_tiles += 1  

        for dr, dc in dir:
            nr, nc = r + dr, c + dc
            if 0 <= nr < row and 0 <= nc < col:
                if grid[nr][nc] != 1 and not visited[nr][nc]:
                    q.append((nr, nc))
    uncl=tot_tiles-cl_tiles
    return cl_tiles,uncl

grid=[[2,0,1],[0,0,0],[1,0,1]]
print(vacc(grid))