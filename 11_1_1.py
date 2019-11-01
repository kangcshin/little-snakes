islands = [[0, 0, 0, 1, 0],
           [0, 1, 1, 0, 0],
           [0, 0, 1, 0, 0],
           [0, 0, 0, 1, 0],
           [0, 0, 0, 1, 0]]

def findBiggestIsland(islands):
    biggestIsland = 0
    def gridSearch(grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != 1:
            return
        grid[i][j] = '*'
        gridSearch(grid, i+1, j)
        gridSearch(grid, i-1, j)
        gridSearch(grid, i, j+1)
        gridSearch(grid, i, j-1)

    for i in range(len(islands)):
        for j in range(len(islands[0])):
            if islands[i][j] == 1:
                gridSearch(islands, i, j)
                biggestIsland += 1
    print(biggestIsland)
    print(islands)


findBiggestIsland(islands)