"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        ''' we do a DFS as usual.
        we will create a node if its not present in the visited map
        we use a map and not a set because we need to make a deep copy, i.e 
        different memory addresses
        '''
        if not node:
            return node
        seen = {}
        def dfs(v):
            if v in seen:
                return seen[v]
            
            clone = Node(v.val)
            seen[v] = clone

            for x in v.neighbors:
                clone.neighbors.append(dfs(x))
            
            return clone
        return dfs(node)
        
        
        