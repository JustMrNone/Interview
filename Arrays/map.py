from collections import deque
from typing import List 

def assignHeights(isWater: List[List[int]]) -> List[List[int]]:
    rows = len(isWater)
    cols = len(isWater[0])
    
    # This is the Result matrix with -1 aka: unvisited cells
    heights = [[-1] * cols for _ in range(rows)]
    
    # init queue for BFS
    bfs_queue = deque()
    
    # Init the queue with all the water cells
    for r in range(rows):
        for c in range(cols):
            if isWater[r][c] == 1:
                bfs_queue.append((r, c))
                # problem concluded that water cells have height 0
                heights[r][c] = 0  
    
    # Directions (north, east, south, west)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # now logically we need to perform the BFS
    while bfs_queue:
        current_row, current_col = bfs_queue.popleft()
        current_height = heights[current_row][current_col]
        
        # now we need to explore neighbors
        for dr, dc in directions:
            neighbor_row, neighbor_col = current_row + dr, current_col + dc
            #FUCKKKKK
            # this shit checks if the neighbor is within bounds and unvisited
            if 0 <= neighbor_row < rows and 0 <= neighbor_col < cols and heights[neighbor_row][neighbor_col] == -1:
                # now assign the height to the neighbor
                heights[neighbor_row][neighbor_col] = current_height + 1
                bfs_queue.append((neighbor_row, neighbor_col))

    return heights

print(assignHeights([[0, 1], [0, 0]]))

print(assignHeights([[0, 0, 1], [1, 0, 0], [0, 0, 0]]))
