"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: 'None' , m={}) -> 'Node' :
        if not node:return None
        if node not in m:
            m[node]=Node(node.val)
            m[node].neighbors=[self.cloneGraph(n,m) for n in node.neighbors]
        return m[node]
        