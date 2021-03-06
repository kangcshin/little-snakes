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
 '''
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2

Given tree t:

   4 
  / \
 1   2

Return true, because t has the same structure and node values with a subtree of s. 
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        
        def isSame(t1, t2):
            if t1 and t2:
                return t1.val == t2.val and isSame(t1.left, t2.left) and isSame(t1.right, t2.right)
            return t1 is t2
        
        if s and t:
            return isSame(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
        
        return s is t
 '''
Given an N-ary tree, find the subtree with the maximum average. Return the root of the subtree.
A subtree of a tree is the node which have at least 1 child plus all its descendants. The average value of a subtree is the sum of its values, divided by the number of nodes.

Example 1:

Input:
		 20
	   /   \
	 12     18
  /  |  \   / \
11   2   3 15  8

Output: 18
Explanation:
There are 3 nodes which have children in this tree:
12 => (11 + 2 + 3 + 12) / 4 = 7
18 => (18 + 15 + 8) / 3 = 13.67
20 => (12 + 11 + 2 + 3 + 18 + 15 + 8 + 20) / 8 = 11.125

18 has the maximum average so output 18.

'''



def maxAverageSubtree(root):
    if not root or not roo.children:
        return None
    
    # averate, number of nodes
    result = [float('-inf'), 0]
    dfs(root)
    
    def dfs(node):
        if not node.children:
            return [node.val, 1]

        temp_sum, temp_num = node.val, 1
        for child in node.children:
            child_sum, child_num = dfs(child)
            temp_sum += child_sum
            temp_num += child_num

        if temp_sum/temp_num > result [0]:
            result = [temp_sum/temp_num, root.val]
        
        return [temp_sum, temp_num]
    
   
    return result[1]

 '''
Top N Competitors
Input:
numCompetitors=6
topNcompetitors=2
competitors=[asdfasdfasdf]
numReviews=6
'''


'''
def top_n_competitors(competitors, reviews, k):
    if not competitors or not reviews:
        return []
    
    # Get counts of competitors in reviews
    counts = {competitor: 0 for competitor in competitors}
    for review in reviews:
        for word in review.split():
            word = word.lower()
            if word in counts:
                counts[word] += 1
    
    # Sort by the count first
    counts = sorted(counts.items(), key = lambda x: x[0])

    # Sort by lexicographical order
    return [word for word, count in sorted(counts, key = lambda x: x[1], reverse = True)][:k]

'''

'''
import heapq
import unittest


def top_n_competitor(top_n_comps, comps, reviews):
    if not top_n_comps or not comps or not reviews:
        return []

    comps_mention = dict()

    for comp in comps:
        comps_mention[comp] = 0

    for review in reviews:
        for word in review.split(" "):
            word = word.lower()
            if word in comps_mention:
                comps_mention[word] += 1

    pq = []
    heapq.heapify(pq)

    for key, val in comps_mention.items():
        heapq.heappush(pq, Comp(key, val))

    return [shop.name for shop in heapq.nsmallest(top_n_comps, pq)]


class Comp:
    def __init__(self, name, num_mentioned):
        self.name = name
        self.num_mentioned = num_mentioned

    def __lt__(self, other):
        # sorted by num_mentioned descending first then name ascending
        return self.name < other.name if self.num_mentioned == other.num_mentioned else self.num_mentioned > other.num_mentioned


class Test(unittest.TestCase):
    def test_n_competitors(self):
        top_n_comps = 2
        comps = ["newshop", "shopnow", "afshion", "fashionbeats", "mymarket", "tcellular"]
        reviews = ["newshop is providing good service in the city;everyone should try newshop",
                   "best services by newshop",
                   "fashionbeats has great services in the city",
                   "Im proud to have fashionbeats",
                   "mymarket has awesome service",
                   "thank Newshop for the quick delivery"]
        self.assertEqual(top_n_competitor(top_n_comps, comps, reviews), ["newshop", "fashionbeats"],
                         "Should return top competitors that have mentioned most in review")

        top_n_comps = 2
        comps = ["newshop", "shopnow", "afshion", "fashionbeats", "mymarket", "tcellular"]
        reviews = ["newshop is providing good service in the city;everyone should try newshop",
                   "best services by newshop",
                   "fashionbeats has great services in the city",
                   "Im proud to have fashionbeats",
                   "afshion has awesome service",
                   "thank afshion for the quick delivery"]
        self.assertEqual(top_n_competitor(top_n_comps, comps, reviews), ["newshop", "afshion"],
                         "Should return top competitors that have mentioned most in review. "
                         "If there is same mentioned number, get the one appear first in alphabetical table")
'''
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
  # Able to move up, down, right, left
  directions = [[1,0], [-1,0], [0,1], [0,-1]]
  q = deque() # Replace with []
  # Storing the index and level information in the queue
  q.append([0, 0, 0])
  while q:
    i, j, level = q.popleft() # Replace queue with [] and pop(0)
    # If the treasure island is found, return the level
    if matrix[i][j] == 'X':
      return level
     # Marking the node as Visited by reusing the 'D' flag
    matrix[i][j] = 'D'
    # Traversing the neighbors
    for dirs in directions:
        x = i + dirs[0]
        y = j + dirs[1]
        if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and matrix[x][y] != 'D':
            q.append((x, y, level+1))
  return -1


inputMap = [['O', 'O', 'O', 'O'],
            ['D', 'O', 'D', 'O'],
            ['O', 'O', 'O', 'O'],
            ['X', 'D', 'D', 'O']]

print(treasureIsland(inputMap))
 '''
You have a map that marks the locations of treasure islands. Some of the map area has jagged rocks and dangerous reefs. Other areas are safe to sail in. There are other explorers trying to find the treasure. So you must figure out a shortest route to one of the treasure islands.

Assume the map area is a two dimensional grid, represented by a matrix of characters. You must start from one of the starting point (marked as S) of the map and can move one block up, down, left or right at a time. The treasure island is marked as X. Any block with dangerous rocks or reefs will be marked as D. You must not enter dangerous blocks. You cannot leave the map area. Other areas O are safe to sail in. Output the minimum number of steps to get to any of the treasure islands.

Example:

Input:
[['S', 'O', 'O', 'S', 'S'],
 ['D', 'O', 'D', 'O', 'D'],
 ['O', 'O', 'O', 'O', 'X'],
 ['X', 'D', 'D', 'O', 'O'],
 ['X', 'D', 'D', 'D', 'O']]

Output: 3
Explanation:
You can start from (0,0), (0, 3) or (0, 4). The treasure locations are (2, 4) (3, 0) and (4, 0). Here the shortest route is (0, 3), (1, 3), (2, 3), (2, 4).
'''

from collections import deque # Can be replaced with []
import sys

def treasureIsland(matrix):
    # Maximum number for default comparison
    result = sys.maxsize
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 'S':
                # Look for closest path to 'X' from every 'S'
                temp = bfs(i, j, matrix)
                # Keep the shortest path
                result = min(result, temp)
    return result

def bfs(i, j, matrix):
    # Storing the index and level information in the queue
    q = deque()
    q.append([i,j,0])
    # Able to move up, down, right, left
    directions = [[1,0], [-1,0], [0,1], [0,-1]]
    while q:
        i, j, level = q.popleft() # pop(0)
        # If the treasure island is found, return the level
        if matrix[i][j] == 'X':
            return level
        # Traversing the neighbors
        for dirs in directions:
            x = i + dirs[0]
            y = j + dirs[1]
            if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and matrix[x][y] != 'D':
                q.append((x, y, level+1))
    return sys.maxsize


inputMap = [['S', 'O', 'O', 'S', 'S'],
            ['D', 'O', 'D', 'O', 'D'],
            ['O', 'O', 'O', 'O', 'X'],
            ['X', 'D', 'D', 'O', 'O'],
            ['X', 'D', 'D', 'D', 'O']]

print(treasureIsland(inputMap))
 '''
Given an int array nums and an int target, find how many unique pairs in the array such that their sum is equal to target. Return the number of pairs.

Example 1:

Input: nums = [1, 1, 2, 45, 46, 46], target = 47
Output: 2
Explanation:
1 + 46 = 47
2 + 45 = 47

Example 2:

Input: nums = [1, 1], target = 2
Output: 1
Explanation:
1 + 1 = 2

Example 3:

Input: nums = [1, 5, 1, 5], target = 6
Output: 1
Explanation:
[1, 5] and [5, 1] are considered the same.

'''

def uniquePairs(nums, target):
    result = set()
    output = set()
    
    for num in nums:
        if target - num in result:
            output.add((num, target-num))
        else:
            result.add(num)
    return len(output)


nums = [1, 1, 2, 45, 46, 46]
target = 47
print(uniquePairs(nums, target))
 '''
Given a 2D grid, each cell is either a zombie 1 or a human 0. Zombies can turn adjacent (up/down/left/right) human beings into zombies every hour. Find out how many hours does it take to infect all humans?

Example:

Input:
[[0, 1, 1, 0, 1],
 [0, 1, 0, 1, 0],
 [0, 0, 0, 0, 1],
 [0, 1, 0, 0, 0]]

Output: 2

Explanation:
At the end of the 1st hour, the status of the grid:
[[1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1],
 [0, 1, 0, 1, 1],
 [1, 1, 1, 0, 1]]

At the end of the 2nd hour, the status of the grid:
[[1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1]]

'''

def zombie(matrix):
    hours, q = 0, []
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                q.append([i, j, 0])
                
    while q:
        x, y, hours = q.pop(0)
        # Able to spread up, down, right, left
        spread_direction = [[1,0], [-1,0], [0,1], [0,-1]]
        for dirs in spread_direction:
            x += dirs[0]
            y += dirs[1]
            if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and matrix[x][y] == 0:
                # Turn to zombie
                matrix[x][y] = 1
                # Save zombie state of next hour
                q.append([x, y, hours+1])
    return hours


input_matrix = [[0, 1, 1, 0, 1],
                [0, 1, 0, 1, 0],
                [0, 0, 0, 0, 1],
                [0, 1, 0, 0, 0]]

print(zombie(input_matrix))
                
     def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        
        low, high = 0, len(height)-1
        ground, rain = 0, 0
        
        while low < high:
            if height[low] <= ground:
                rain += (ground - height[low])
                low += 1
            elif height[high] <= ground:
                rain += (ground - height[high])
                high -= 1
            else:
                ground = min(height[low], height[high])
        return rain
 from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if len(self.cache) >= self.capacity and key not in self.cache:
            self.cache.popitem(last=False)
        self.cache[key] = value
        self.cache.move_to_end(key)
     def longestPalindrome(self, s: str) -> str:
        out = ''
        for i in range(len(s)):
            out = max(self.helper(s,i,i), self.helper(s,i,i+1), out, key=len)
        return out
    
    def helper(self,s,l,r):
        while 0 <= l and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]
     def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0
        
        def dfs(grid, i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
                return
            grid[i][j] = '*'
            dfs(grid, i+1, j)
            dfs(grid, i-1, j)
            dfs(grid, i, j+1)
            dfs(grid, i, j-1)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(grid, i, j)
                    num_islands += 1
                    
        return num_islands
 from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = defaultdict(list)
        for s in strs:
            temp = ''.join(sorted(s))
            answer[temp].append(s)
        return answer.values()
        
 class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        map_new = collections.defaultdict(lambda:Node(0, None, None))
        map_new[None] = None
        
        node_old = head
        while node_old:
            map_new[node_old].val = node_old.val
            map_new[node_old].next = map_new[node_old.next]
            map_new[node_old].random = map_new[node_old.random]
            node_old = node_old.next
        return map_new[head]
     def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def toint(node):
            return node.val + 10 * toint(node.next) if node else 0
        n = toint(l1) + toint(l2)
        first = last = ListNode(n % 10)
        while n > 9:
            n /= 10
            last.next = last = ListNode(n % 10)
        return first
 from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if len(self.cache) >= self.capacity and key not in self.cache:
            self.cache.popitem(last=False)
        self.cache[key] = value
        self.cache.move_to_end(key)
 class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0
        
        def dfs(grid, i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
                return
            
            grid[i][j] = '#'
            
            dfs(grid, i+1, j)
            dfs(grid, i-1, j)
            dfs(grid, i, j+1)
            dfs(grid, i, j-1)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    num_islands += 1
                    dfs(grid, i, j)
        return num_islands
 class Solution:
    def longestPalindrome(self, s: str) -> str:
        answer = ''
        
        def helper(s,left, right):
            while 0 <= left and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]
        
        
        for i in range(len(s)):
            answer = max(helper(s,i,i), helper(s,i,i+1), answer, key=len)
            
        return answer

 class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        output = 0
        pointer = 0
        seen = {}
        
        for idx, c in enumerate(s):
            if c in seen and pointer <= seen[c]:
                pointer = seen[c] + 1
            else:
                output = max(output, idx-pointer+1)
            seen[c] = idx
            
        return output
                
 """
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        copy_map = collections.defaultdict(lambda:Node(0, None, None))
        copy_map[None] = None
        
        node_old = head
        while node_old:
            copy_map[node_old].val = node_old.val
            copy_map[node_old].next = copy_map[node_old.next]
            copy_map[node_old].random = copy_map[node_old.random]
            node_old = node_old.next
        return copy_map[head]
        
    
 class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        rooms = []
        intervals.sort(key=lambda x: x[0])
        heapq.heappush(rooms, intervals[0][1])
        
        for i in intervals[1:]:
            if rooms[0] <= i[0]:
                heapq.heappop(rooms)
            heapq.heappush(rooms, i[1])
            
        return len(rooms)
 class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        points.sort(key=lambda points: points[0]**2+points[1]**2)
        return points[:K]
        
 from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = defaultdict(list)
        for s in strs:
            temp = ''.join(sorted(s))
            answer[temp].append(s)
        return answer.values()

 from random import choice
class RandomizedSet():
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}
        self.list = []

        
    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.dict:
            return False
        self.dict[val] = len(self.list)
        self.list.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.dict:
            # move the last element to the place idx of the element to delete
            last_element, idx = self.list[-1], self.dict[val]
            self.list[idx], self.dict[last_element] = last_element, idx
            # delete the last element
            self.list.pop()
            del self.dict[val]
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return choice(self.list)
 class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.board = collections.Counter()
        self.size = n

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """

        for i, x in enumerate((row, col, row+col, row-col)):
            self.board[i, x, player] += 1
            # print(self.board)
            if self.board[i, x, player] == self.size:
                # print(self.board)
                return player
        return 0
    
# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
 class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for n in nums:
            counter[n] = counter.get(n, 0) + 1
        sorted_counter = sorted(counter, key=lambda x: counter[x], reverse=True)
        
        return sorted_counter[:k]
        
 class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = {}
        answer = []
        for word in words:
            counter[word] = counter.get(word, 0) + 1
        sorted_counter = sorted(counter.items(), key=lambda item: (-item[-1], item[0]))
        
        for i in range(k):
            answer.append(sorted_counter[i][0])
            
        return answer
 class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        output, level, direction = [], [root], 1
        
        while level:
            output.append([n.val for n in level][::direction])
            direction *= -1
            level = [child for node in level for child in (node.left, node.right) if child]
        
        return output
 class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        
        def nextday(cells):
            newcells=[]
            newcells.append(0)
            for i in range(1, len(cells)-1):
                if cells[i-1] == cells[i+1]:
                    newcells.append(1)
                else:
                    newcells.append(0)
            newcells.append(0)
            return newcells
        
        seen = {}
        while N > 0:
            c = tuple(cells)
            if c in seen:
                N %= seen[c]-N
            seen[c] = N
            
            if N >= 1:
                N -= 1
                cells = nextday(cells)
                
        return cells
 class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        # a3 stores the second largest element
        a3 = float('-inf')
        #stack.top() stores the largest element
        stack = []
        
        for a in nums[::-1]:
            if a < a3:
                return True
            while stack and a > stack[-1]:
                a3 = stack.pop()
            stack.append(a)
        return False
 # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        
        if not root:
            return []
        
        output = [root.val]
        
        def dfs(root, isleft, isright):
            if root:
                # append when going down from the left or at leaf node
                if (not root.left and not root.right) or isleft:
                    output.append(root.val)
                if root.left and root.right:
                    dfs(root.left, isleft, False)
                    dfs(root.right, False, isright)
                else:
                    dfs(root.left, isleft, isright)
                    dfs(root.right, isleft, isright)
                # append to boundary when coming up from the right
                if (root.left or root.right) and isright:
                    output.append(root.val)
                    
        dfs(root.left, True, False)
        dfs(root.right, False, True)
        
        return output

 class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        output, pointer = 0, 0
        seen = {}
        
        for idx, c in enumerate(s):
            if c in seen and pointer <= seen[c]:
                pointer = seen[c]+1
            else:
                # print(idx-pointer)
                output = max(output, idx-pointer+1)
                # print(output)
            seen[c] = idx
            
        return output
                
 class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        begin, end = 0, len(height)-1
        
        while begin < end:
            h = height[begin] if height[begin] < height[end] else height[end]
            area = max(area, h*(end-begin))
            if height[begin] < height[end]:
                begin += 1
            else:
                end -= 1
            
        return area
 class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        for i in range(len(nums)-2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i+1, len(nums)-1
            while left < right:
                # print(left, right)
                if nums[i] + nums[left] + nums[right] == 0:
                    output.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    right -= 1
                    
        return output
 class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = j = len(nums)-1
        while i > 0 and nums[i] <= nums[i-1]:
            i -= 1
        if i > 0:
            while nums[j] <= nums[i-1]:
                j -= 1
            nums[i-1], nums[j] = nums[j], nums[i-1]
        # print(nums)
        nums[i:] = reversed(nums[i:])
  
 class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix.reverse()
        print(matrix)
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        return matrix
 class Solution:
    def canJump(self, nums: List[int]) -> bool:
        pointer = len(nums)-1
        while pointer != 0:
            for i in reversed(range(pointer)):
                if pointer-i <= nums[i]:
                    pointer = i
                    break
                if i == 0:
                    return False
        return True
 class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        number = 1
        
        for i in reversed(range(len(digits))):
            out = digits[i] + number + carry
            carry = out // 10
            out = out % 10
            digits[i] = out
            
            if number:
                number = 0
        if carry:
            digits.insert(0,carry)
        
        return digits
        
    def minWindows(s, t):
        need = collections.Counter(t)
        missing = len(t)
        start, end = 0, 0
        i = 0

        for j, char in enumerate(s, 1):
            if need[char] > 0:
                missing -= 1
            need[char] -= 1
            if missing == 0:
                while i < j and need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1
                need[s[i]] += 1
                missing += 1
                if end == 0 or j-i < end-start:
                    start, end = i, j
                i += 1
        return s[start:end]


class Solution:
    def __init__(self):
        self.queue = []
        
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        out = 0
        count = n
        buffer = [' ']*4
        
        while count > 0:
            k = read4(buffer)
            # print(k)
            self.queue.extend(buffer[:k])
            # print(self.queue)
            count = min(len(self.queue), n-out)
            buf[out:out+count] = [self.queue.pop(0) for _ in range(count)]
            out += count

        return out

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        output = 0
        begin, end = 0, 0
        
        while end < len(s):
            if len(s) == 1:
                return 1
            while len(set(s[begin:end+1])) > 2 and begin < end:
                begin += 1
            output = max(output, end-begin+1)
            end += 1
            
        return output

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        out = []
        
        nums.append(upper+1)
        pre = lower -1
        
        for num in nums:
            if num == pre+2:
                out.append(str(num-1))
            if num > pre+2:
                out.append(str(pre+1) + '->' + str(num-1))
            pre = num
            
        return out

class Solution:
    def nextClosestTime(self, time: str) -> str:
        h, m = time.split(':')
        current = int(h) * 60 + int(m)
        out = None
        
        for i in range(current+1, current+1441):
            t = i % 1440
            h, m = t // 60, t % 60
            out = '%02d:%02d' % (h, m)
            
            if set(out) <= set(time):
                break
        return out

class Solution:
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        for idx, source, target in sorted(zip(indexes, sources, targets), reverse=True):
            if S[idx:idx+len(source)] == source:
                S = S[:idx] + target + S[idx+len(source):]
            
        return S

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        output = 0
        pointer = -1
        
        for i in range(len(seats)):
            if seats[i]:
                output = max(output, i if pointer < 0 else (i-pointer)//2)
                pointer = i
        return max(output, len(seats)-pointer-1)

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for c in s:
            if c == ')':
                if not stack or stack[-1] != '(':
                    return False
                stack.pop()
            elif c == '}':
                if not stack or stack[-1] != '{':
                    return False
                stack.pop()
            elif c == ']':
                if not stack or stack[-1] != '[':
                    return False
                stack.pop()
            else:
                stack.append(c)
        if len(stack) != 0:
            return False
        
        return True
   
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return
        if len(lists) == 1:
            return lists[0]
        
        def merge(left, right):
            temp = current = ListNode(0)
            while left and right:
                if left.val < right.val:
                    current.next = left
                    left = left.next
                else:
                    current.next = right
                    right = right.next
                current = current.next
            current.next = left or right
            
            return temp.next

        mid = len(lists) // 2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])
        
        return merge(left, right)

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = collections.Counter(t)
        missing = len(t)
        start, end, i = 0, 0, 0
        
        for j, char in enumerate(s, 1):
            if need[char] > 0:
                missing -= 1
            need[char] -= 1
            if missing == 0:
                while i < j and need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1
                need[s[i]] += 1
                missing += 1
                if end == 0 or j-i < end-start:
                    start,end = i,j
                i += 1
        return s[start:end]


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return
        if len(lists) == 1:
            return lists[0]
        
        def helper(left, right):
            temp = current = ListNode(0)
            while left and right:
                if left.val < right.val:
                    current.next = left
                    left = left.next
                else:
                    current.next = right
                    right = right.next
                current = current.next
            current.next = left or right
            return temp.next
        
        mid = len(lists) // 2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])
        
        return helper(left, right)
    
    class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        output = []
        
        for interval in intervals:
            if not output or output[-1][1] < interval[0]:
                output.append(interval)
            else:
                output[-1][1] = max(output[-1][1], interval[1])

                
        return output


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        left, right = 1, 1
        
        for i in range(len(nums)):
            output[i] *= left
            left *= nums[i]
            output[~i] *= right
            right *= nums[~i]
            
        return output
        
        
