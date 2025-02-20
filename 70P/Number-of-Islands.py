from collections import deque

grid1 = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
grid2 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

def number_of_islands(grid):
    if not grid:
        return 0
    
    def bfs(r, c):
        q = deque()
        visit.add((r, c))
        q.append((r, c))
    
        while q:
            row, col = q.popleft() 
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            
            for dr, dc in directions:
                r, c = row+dr, col+dc
                
                if (r in range(rows) and c in range(cols) and grid[r][c] == '1' and (r, c) not in visit):
                    q.append((r, c))
                    visit.add((r, c))
    
    count = 0
    rows = len(grid)
    cols = len(grid[0])
    visit = set()
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1' and (r, c) not in visit:
                bfs(r, c)
                count+=1
    return count 


ex1 = number_of_islands(grid1)
ex2 = number_of_islands(grid2)
print(ex1)

def bfs(grid, r, c, visit):
    q = deque()
    visit.add((r, c))
    q.append((r, c))

    rows = len(grid)
    cols = len(grid[0])

    while q:
        row, col = q.popleft()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        for dr, dc in directions:
            nr, nc = row + dr, col + dc

            if (nr in range(rows) and nc in range(cols) and grid[nr][nc] == '1' and (nr, nc) not in visit):
                q.append((nr, nc))
                visit.add((nr, nc))

def number_of_island2(grid):
    if not grid:
        return 0

    count = 0
    rows = len(grid)
    cols = len(grid[0])
    visit = set()
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1' and (r, c) not in visit:
                bfs(grid, r, c, visit)
                count += 1

    return count

print("ass")
print(number_of_island2(grid2))