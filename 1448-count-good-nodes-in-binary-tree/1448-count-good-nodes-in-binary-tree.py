# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, max_so_far: int) -> int:
            if not node:
                return 0
            
            # Determine if the current node is "good"
            is_good = 0
            if node.val >= max_so_far:
                is_good = 1
                # Update the running maximum for the path ahead
                max_so_far = node.val
            
            # Recursively count good nodes in the left and right subtrees
            left_count = dfs(node.left, max_so_far)
            right_count = dfs(node.right, max_so_far)
            
            # Return total good nodes found in this subtree
            return is_good + left_count + right_count
            
        # Start the DFS with the root node. 
        # The initial maximum value is the root's own value.
        return dfs(root, root.val)