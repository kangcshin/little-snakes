'''
Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]

'''

# def generateMatrix(n):
#     matrix = [[None] * n for _ in range(n)]
    
#     i, j, dir_x, dir_y = 0, 0, 0, 1
    
#     for currentNum in range(1, n*n+1):
#         matrix[i][j] = currentNum
        
#         print((i+dir_x)%n, (j+dir_y)%n)
#         if matrix[(i+dir_x)%n][(j+dir_y)%n]:
#             print('turn')
#             dir_x, dir_y = dir_y, -dir_x
        
#         i += dir_x
#         j += dir_y

#     return matrix


def generateMatrix(n):
    matrix, nums = [], n*n+1
    while nums > 1:
        nums, endNum = nums-len(matrix), nums
        # rotate clockwise and add top row, add nums in reverse order
        matrix = [[i for i in range(nums,endNum)]] + [list(j) for j in zip(*matrix[::-1])]
        
    return matrix


print(generateMatrix(3))