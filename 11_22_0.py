'''
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

 

Example 1:

Input:
{"$id":"1","next":{"$id":"2","next":null,"random":{"$ref":"2"},"val":2},"random":{"$ref":"2"},"val":1}

Explanation:
Node 1's value is 1, both of its next and random pointer points to Node 2.
Node 2's value is 2, its next pointer points to null and its random pointer points to itself.

'''



# # @param head, a RandomListNode
# # @return a RandomListNode
# def copyRandomList(head):
#     copy = collections.defaultdict(lambda:RandomListNode(0))
#     copy[None] = None
#     node = head
    
#     while node:
#         copy[node].label = node.label
#         copy[node].next = copy[node.next]
#         copy[node].random = copy[node.random]
#         node = node.next
        
#     return copy[head]


"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        """dict with old Nodes as keys and new Nodes as values. Doing so allows us to create node's next and random as we iterate through the list from head to tail. Otherwise, we need to go through the list backwards.
        defaultdict() is an efficient way of handling missing keys """ 
        map_new = collections.defaultdict(lambda: Node(None, None, None))
        map_new[None] = None # if a node's next or random is None, their value will be None but not a new Node, doing so removes the if-else check in the while loop
        
        nd_old = head
        while nd_old:
            map_new[nd_old].val = nd_old.val
            map_new[nd_old].next = map_new[nd_old.next]
            map_new[nd_old].random = map_new[nd_old.random]
            nd_old = nd_old.next
        return map_new[head]
    