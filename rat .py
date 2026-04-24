def dfs(grid, visited, i, j, row, col, path,res):
    if i == row - 1 and j == col - 1:
        res.append(path)
        return
    directions = [(0, 1, 'R'), (1, 0, 'D')]
    for di, dj,p in directions:
        ni= i + di
        nj= j + dj
        if 0 <= ni < row and 0 <= nj < col and grid[ni][nj] == 1 and not visited[ni][nj]:
            visited[ni][nj] = True
            dfs(grid, visited, ni, nj, row, col, path + p,res)
            visited[ni][nj] = False

def rat_in_maze(grid):
    row, col = len(grid), len(grid[0])
    visited = [[False for _ in range(col)] for _ in range(row)]
    res = []
    if grid[0][0] == 1:
        visited[0][0] = True
        dfs(grid, visited, 0, 0, row, col, '', res)
    return res

maze = [
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 1, 0, 0],
    [1, 1, 1, 1]
]

result = rat_in_maze(maze)
print(result)