'''
There's an undirected connected graph with n nodes labeled 1..n. But some of the edges has been broken disconnecting the graph. Find the minimum cost to repair the edges so that all the nodes are once again accessible from each other.

Input:

    n, an int representing the total number of nodes.
    edges, a list of integer pair representing the nodes connected by an edge.
    edgesToRepair, a list where each element is a triplet representing the pair of nodes between which an edge is currently broken and the cost of repearing that edge, respectively (e.g. [1, 2, 12] means to repear an edge between nodes 1 and 2, the cost would be 12).

Example 1:

Input: n = 5, edges = [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]], edgesToRepair = [[1, 2, 12], [3, 4, 30], [1, 5, 8]]
Output: 20
Explanation:
There are 3 connected components due to broken edges: [1], [2, 3] and [4, 5].
We can connect these components into a single component by repearing the edges between nodes 1 and 2, and nodes 1 and 5 at a minimum cost 12 + 8 = 20.

Example 2:

Input: n = 6, edges = [[1, 2], [2, 3], [4, 5], [3, 5], [1, 6], [2, 4]], edgesToRepair = [[1, 6, 410], [2, 4, 800]]
Output: 410

Example 3:

Input: n = 6, edges = [[1, 2], [2, 3], [4, 5], [5, 6], [1, 5], [2, 4], [3, 4]], edgesToRepair = [[1, 5, 110], [2, 4, 84], [3, 4, 79]]
Output: 79

'''


def minimumCost(n, edges, edgesToRepair):
    parent = {i:i for i in range(1, n+1)}
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        parent[find(x)] = find(y)
        
    def isUnion(x, y):
        return find(x) == find(y)
    
    repairMap = []
    
    for edge in edgesToRepair:
        repairMap.append(edge[0:2])
        
    node_list = [node for node in edges if node not in repairMap]
    
    # Connect current edges
    for x, y in node_list:
        if not isUnion(x, y):
            union(x, y)
    
    result = 0
    
    edgesToRepair.sort(key = lambda x: x[2])
    
    for node1, node2, cost in edgesToRepair:
        if not isUnion(node1, node2):
            union(node1, node2)
            result += cost
    
    return result
    # return -1 if len(set(find(x) for x in range(1, n+1))) > 1 else result


n = 6
edges = [[1, 2], [2, 3], [4, 5], [5, 6], [1, 5], [2, 4], [3, 4]]
newedges = [[1, 5, 110], [2, 4, 84], [3, 4, 79]]
print(minimumCost(n, edges, newedges))
    
    
    
    
