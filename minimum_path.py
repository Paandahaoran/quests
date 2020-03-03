import numpy as np
grid = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]

def miniPathSum(grid):
    for x in range(1,np.shape(grid)[1]):
        grid[0][x] = grid[0][x] + grid[0][x-1]
    for y in range(1,np.shape(grid)[1]):
        grid[y][0] = grid[y][0] + grid[y-1][0]
    for i in range(1,np.shape(grid)[0]):
        for j in range(1,np.shape(grid)[1]):
            grid[i][j] = min(grid[i-1][j] + grid[i][j],grid[i][j] + grid[i][j-1])
    print(grid)
    return grid[-1][-1]


print(miniPathSum(grid))
