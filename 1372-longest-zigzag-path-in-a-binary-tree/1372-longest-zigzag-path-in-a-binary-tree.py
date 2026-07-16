# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.max_path = 0

        def dfs(node):
            if not node:
                # Return -1 because a path length is counted by edges. 
                # An empty node adds an edge that doesn't exist, which cancels out when we add 1.
                return -1, -1
            
            # Recursively get the zigzag lengths from left and right subtrees
            _, left_right = dfs(node.left)
            right_left, _ = dfs(node.right)
            
            # To go left from the current node, we must continue the path 
            # that went right from the left child.
            current_left = left_right + 1
            
            # To go right from the current node, we must continue the path 
            # that went left from the right child.
            current_right = right_left + 1
            
            # Update the global maximum path found so far
            self.max_path = max(self.max_path, current_left, current_right)
            
            # Return lengths starting from this node going left and right
            return current_left, current_right

        dfs(root)
        return self.max_path