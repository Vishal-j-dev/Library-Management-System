from collections import deque

def orangesRotting(grid):
    if not grid or not grid[0]:
        return -1

    rows, cols = len(grid), len(grid[0])
    q = deque()
    fresh = 0

    # Collect initial rotten oranges and count fresh ones
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 2:
                q.append((i, j))
            elif grid[i][j] == 1:
                fresh += 1

    if fresh == 0:
        return 0

    minutes = 0
    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    while q and fresh > 0:
        # Process all rotten oranges at the current minute
        for _ in range(len(q)):
            x, y = q.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                    grid[nx][ny] = 2
                    fresh -= 1
                    q.append((nx, ny))
        minutes += 1

    return minutes if fresh == 0 else -1

    # Take input from user
r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))

print("Enter the grid values row by row (0=empty, 1=fresh, 2=rotten):")
grid = []
for _ in range(r):
    row = list(map(int, input().split()))
    grid.append(row)

result = orangesRotting(grid)
print("Minimum minutes to rot all oranges:", result)