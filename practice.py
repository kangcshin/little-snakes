'''
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1

Example 2:

Input:
11000
11000
00100
00011

Output: 3

'''

def numIslands(matrix):
    result = 0  
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == '1':
                dfs(i, j, matrix)
                result += 1
    return result

def dfs(i, j, matrix):
    if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]) or matrix[i][j] != '1':
        return
    matrix[i][j] = '*'
    dfs(i+1, j, matrix)
    dfs(i-1, j, matrix)
    dfs(i, j+1, matrix)
    dfs(i, j-1, matrix)

island_map = [['1','1','0','0','0'],
              ['1','1','0','0','0'],
              ['0','0','1','0','0'],
              ['0','0','0','1','1']]

print(numIslands(island_map))

############################################################################################################

