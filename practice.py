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

'''
A string S of lowercase letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

Example 1:

Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.

Note:

    S will have length in range [1, 500].
    S will consist of lowercase letters ('a' to 'z') only.

'''

def partitionLabels(S):
    """
    :type S: str
    :rtype: List[int]
    """
    dic = {}
    for i, char in enumerate(S):
        dic[char] = i
    res = []
    currLen = 0
    hi = 0
    for i, char in enumerate(S):
        hi = max(hi, dic[char])
        if i == hi:
            res.append(i - currLen + 1)
            currLen = i+1
    return res

S = "ababcbacadefegdehijhklij"
print(partitionLabels(S))

############################################################################################################

'''
There are 8 prison cells in a row, and each cell is either occupied or vacant.

Each day, whether the cell is occupied or vacant changes according to the following rules:

    If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.
    Otherwise, it becomes vacant.

(Note that because the prison is a row, the first and the last cells in the row can't have two adjacent neighbors.)

We describe the current state of the prison in the following way: cells[i] == 1 if the i-th cell is occupied, else cells[i] == 0.

Given the initial state of the prison, return the state of the prison after N days (and N such changes described above.)

 

Example 1:

Input: cells = [0,1,0,1,1,0,0,1], N = 7
Output: [0,0,1,1,0,0,0,0]
Explanation: 
The following table summarizes the state of the prison on each day:
Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
Day 7: [0, 0, 1, 1, 0, 0, 0, 0]

Example 2:

Input: cells = [1,0,0,1,0,0,1,0], N = 1000000000
Output: [0,0,1,1,1,1,1,0]

'''

def prisonAfterNDays(cells, N):
    def nextday(cells):
        newcells =[]
        newcells.append(0)
        for i in range(1, len(cells)-1):
            if cells[i - 1] == cells[i + 1]:
                newcells.append(1)
            else:
                newcells.append(0)
        newcells.append(0)
        return newcells

    seen = {}
    while N > 0:
        c = tuple(cells)
        if c in seen:
            N %= seen[c] - N
        seen[c] = N

        if N >= 1:
            N -= 1
            cells = nextday(cells)

    return list(cells)

cells = [0,1,0,1,1,0,0,1]
N = 7

# cells = [1,0,0,1,0,0,1,0]
# N = 1000000000
print(prisonAfterNDays(cells, N))

############################################################################################################
'''
Description:
Implement a function to return product suggestions using products from a product repository after each character is typed by the customer in the search bar.
If there are more than THREE acceptable products, return the product name that is first in the alphabetical order.
Only return product suggestions after the customer has entered two characters.
Product suggestions must start with the characters already typed.
Both the repository and the customer query should be compared in a CASE-INSENSITIVE way.

Input:
The input to the method/function consist of three arguments:

    numProducts, an integer representing the number of various products in Amazon's product repository;
    repository, a list of unique strings representing the various products in Amazon's product repository;
    customerQuery, a string representing the full search query of the customer.

Output:
Return a list of a list of strings, where each list represents the product suggestions made by the system as the customer types each character of the customerQuery. Assume the customer types characters in order without deleting/removing any characters.

Example:
Input:
numProducts = 5
repository = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
customerQuery = "mouse"

Output:
[["mobile", "moneypot", "monitor"],
["mouse", "mousepad"],
["mouse", "mousepad"],
["mouse", "mousepad"]]

Explanation:
The chain of words that will generate in the search box will be mo, mou, mous and mouse, and each
line from output shows the suggestions of "mo", "mou", "mous" and "mouse", respectively in each line.
For the suggestions that are generated for "mo", the matches that will be generated are:
["mobile", "mouse", "moneypot", "monitor", "mousepad"]. Alphabetically, they will be reordered to
["mobile", "moneypot", "monitor", "mouse", "mousepad"]. Thus, the suggestions are ["mobile", "moneypot", "monitor"]
'''

def productSuggestion(numProducts, repository, customQuery):
    sortedRepository = sorted(repository)
    output, bucket = [], []
    for i in range(2, len(customQuery)+1):
        for j in range(numProducts):
            if customQuery[0:i] == sortedRepository[j][0:i]:
                bucket.append(sortedRepository[j])
        if len(bucket) > 3:
            output.append(bucket[0:3])
        else:
            output.append(bucket)
        bucket = []
    return output


repo = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
query = "mouse"
print(productSuggestion(5, repo, query))

############################################################################################################
'''
A six-sided die is a small cube with a different number of pips on each face (side), ranging from 1 to 6.
On any two opposite side of the cube, the number of pips adds up to 7; that is, there are three pairs of opposite sides: 1 and 6, 2 and 5, and 3 and 4.
There are N dice lying on a table, each showing the pips on its top face. In one move, you can take one die and rotate it to an adjacent face.
For example, you can rotate a die that shows 1 s that it shows 2, 3, 4 or 5. However, it cannot show 6 in a single move, because the faces with one pip and six pips visible are opposite sides rather than adjacent.
You want to show the same number of pips on the top face of all N dice. Given that each of the dice can be moved multiple times, count the minimum number of moves needed to get equal faces.

Write a function that, given an array A consisting of N integers describing the number of pips (from 1 to 6) shown on each die's top face, returns the minimum number of moves necessary for each die show the same number of pips.

Example 1:

Input: A = [1, 2, 3]
Output: 2
Explanation: You can pick the first two dice and rotate each of them in one move so that they all show three pips on the top face.
Notice that you can also pick any other pair of dice in this case.

Example 2:

Input: A = [1, 1, 6]
Output: 2
Explanation: The only optimal answer is to rotate the last die so that it shows one pip. It is necessary to use two rotations to achieve this.

Example 3:

Input: A = [1, 6, 2, 3]
Output: 3
Explanation: For instance, you can make all dice show 2: just rotate each die which is not showing 2.
Notice that for each die you can do this in one move.

A ssume that:
• N is an integer within the range [1..100];
• each element of the array A is an integer within the range [1..6].
'''

# import math

def rollDice(A):
    count = [0] * 7
    for i in A:
        count[i] += 1
    min_rotation = float('inf') #math.inf
    for i in range(1,7):
        rotate = sum(count) - count[i] + count[7-i]
        if rotate < min_rotation:
            min_rotation = rotate
    return min_rotation

A = [1,6,2,3]
print(rollDice(A))
############################################################################################################
'''
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

    Integers in each row are sorted in ascending from left to right.
    Integers in each column are sorted in ascending from top to bottom.

Example:

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

Given target = 5, return true.

Given target = 20, return false.

'''
# Brute Force Way (Check every element in matrix)
# def searchMatrix(matrix, target):
#     if not matrix or not target:
#         return False
#     for i in range(len(matrix)):
#         for j in range(len(matrix[0])):
#             if matrix[i][j] == target:
#                 return True
#     return False

def searchMatrix(matrix, target):
#     if not matrix or not target:
#         return False
    
    col, row = len(matrix)-1, 0
    
    while col >= 0 and row < len(matrix[0]):
        if matrix[col][row] == target:
            return True
        elif matrix[col][row] < target:
            row += 1
        else:
            col -= 1
                
    return False



matrix = [[1,   4,  7, 11, 15],
          [2,   5,  8, 12, 19],
          [3,   6,  9, 16, 22],
          [10, 13, 14, 17, 24],
          [18, 21, 23, 26, 30]]

print(searchMatrix(matrix, 20))
############################################################################################################
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
############################################################################################################
'''
Given a string s and an int k, return all unique substrings of s of size k with k distinct characters.

Example 1:

Input: s = "abcabc", k = 3
Output: ["abc", "bca", "cab"]

Example 2:

Input: s = "abacab", k = 3
Output: ["bac", "cab"]

Example 3:

Input: s = "awaglknagawunagwkwagl", k = 4
Output: ["wagl", "aglk", "glkn", "lkna", "knag", "gawu", "awun", "wuna", "unag", "nagw", "agwk", "kwag"]
Explanation: 
Substrings in order are: "wagl", "aglk", "glkn", "lkna", "knag", "gawu", "awun", "wuna", "unag", "nagw", "agwk", "kwag", "wagl" 
"wagl" is repeated twice, but is included in the output once.

'''

def substringk(s, k):
    if not s or k == 0:
        return []
    
    letter, res = {}, set()
    start = 0
    for i in range(len(s)):
        if s[i] in letter and letter[s[i]] >= start:
            start = letter[s[i]]+1
        letter[s[i]] = i
        if i-start+1 == k:
            res.add(s[start:i+1])
            start += 1
    return list(res)

s = "awaglknagawunagwkwagl"
k = 4
print(substringk(s, k))
############################################################################################################
'''
Given a string s and an int k, return an int representing the number of substrings (not unique) of s with exactly k distinct characters. If the given string doesn't have k distinct characters, return 0.
https://leetcode.com/problems/subarrays-with-k-different-integers

Example 1:

Input: s = "pqpqs", k = 2
Output: 7
Explanation: ["pq", "pqp", "pqpq", "qp", "qpq", "pq", "qs"]

Example 2:

Input: s = "aabab", k = 3
Output: 0

Constraints:

    The input string consists of only lowercase English letters [a-z]
    0 ≤ k ≤ 26

'''

def subStrings(s, k):
    if k > len(set(s)):
        return 0
    
    result = 0
    
    for i in range(len(s)):
        dist = set()
        for j in range(i, len(s)):
            if s[j] not in dist:
                dist.add(s[j])
            if len(dist) == k:
                result += 1
            elif len(dist) > k:
                break
    return result

s = 'pqpqs'
k = 2

print(subStrings(s, k))
############################################################################################################
