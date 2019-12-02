'''
Given a matrix with r rows and c columns, find the maximum score of a path starting at [0, 0] and ending at [r-1, c-1]. The score of a path is the minimum value in that path. For example, the score of the path 8 → 4 → 5 → 9 is 4.

Don't include the first or final entry. You can only move either down or right at any point in time.

Example 1:

Input:
[[5, 1],
 [4, 5]]

Output: 4
Explanation:
Possible paths:
5 → 1 → 5 => min value is 1
5 → 4 → 5 => min value is 4
Return the max value among minimum values => max(4, 1) = 4.

Example 2:

Input:
[[1, 2, 3]
 [4, 5, 1]]

Output: 4
Explanation:
Possible paths:
1-> 2 -> 3 -> 1
1-> 2 -> 5 -> 1
1-> 4 -> 5 -> 1
So min of all the paths = [2, 2, 4]. Note that we don't include the first and final entry.
Return the max of that, so 4.

'''
# DP Solution
def max_min_path(matrix):
    if not matrix:
        return 0
    # So they are not considered
    matrix[0][0], matrix[-1][-1] = sys.maxsize, sys.maxsize
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(i, j)
            if i > 0 and j > 0:
                matrix[i][j] = max(min(matrix[i-1][j], matrix[i][j]), min(matrix[i][j-1], matrix[i][j]))
                # print(matrix)
            elif i > 0:
                matrix[i][j] = min(matrix[i-1][j], matrix[i][j])
            elif j > 0:
                matrix[i][j] = min(matrix[i][j-1], matrix[i][j])
                
    return matrix[-1][-1]
                

input_matrix = [[1, 2, 3],
                [4, 5, 1]]

print(max_min_path(input_matrix))
