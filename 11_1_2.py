islands = [[0, 0, 0, 1, 0],
           [0, 1, 1, 0, 0],
           [0, 0, 1, 0, 0],
           [0, 0, 0, 1, 0],
           [0, 0, 0, 1, 0]]

def findBiggestIsland(islands):
    length, width = len(islands), len(islands[0])


    def dfs(i, j):
        if 0 <= i < length and 0 <= j < width and islands[i][j]==1:
           islands[i][j] = '*'
           return 1 + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i + 1, j) + dfs(i, j - 1)
        return 0
    
    maxArea = 0
    for i in range(length):
        for j in range(width):
            maxArea = max(dfs(i, j), maxArea)

    print(maxArea)
        


findBiggestIsland(islands)