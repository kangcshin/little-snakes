'''
You have a map that marks the location of a treasure island. Some of the map area has jagged rocks and dangerous reefs. Other areas are safe to sail in. There are other explorers trying to find the treasure. So you must figure out a shortest route to the treasure island.

Assume the map area is a two dimensional grid, represented by a matrix of characters. You must start from the top-left corner of the map and can move one block up, down, left or right at a time. The treasure island is marked as X in a block of the matrix. X will not be at the top-left corner. Any block with dangerous rocks or reefs will be marked as D. You must not enter dangerous blocks. You cannot leave the map area. Other areas O are safe to sail in. The top-left corner is always safe. Output the minimum number of steps to get to the treasure.

Example:

Input:
[['O', 'O', 'O', 'O'],
 ['D', 'O', 'D', 'O'],
 ['O', 'O', 'O', 'O'],
 ['X', 'D', 'D', 'O']]

Output: 5
Explanation: Route is (0, 0), (0, 1), (1, 1), (2, 1), (2, 0), (3, 0) The minimum route takes 5 steps.
'''


from collections import deque

def treasureIsland(matrix):
  # If starting index itself is the 'D'
  if matrix[0][0] == 'D':
    return -1
  q = deque()
  # storing the index and level information in the queue
  q.append([0, 0, 0])
  while q:
    i, j, level = q.popleft()
    # If the treasure island is found, return the level
    if matrix[i][j] == 'X':
      return level
     # Marking the node as Visited by reusing the 'D' flag
    matrix[i][j] = 'D'
     # Traversing the neighbors
    for x, y in [(i-1, j),(i+1, j), (i, j-1), (i, j+1)]:
      if x >= 0 and x < len(matrix) and y >= 0 and y < len(matrix[0]) and matrix[x][y] != 'D' :
        q.append([x, y, level+1])
  return -1


inputMap = [['O', 'O', 'O', 'O'],
            ['D', 'O', 'D', 'O'],
            ['O', 'O', 'O', 'O'],
            ['X', 'D', 'D', 'O']]

print(treasureIsland(inputMap))