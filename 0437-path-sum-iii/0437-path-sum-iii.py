# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix_sums = defaultdict(int)
        prefix_sums[0] = 1
        
        def dfs(node: Optional[TreeNode], current_sum: int) -> int:
            if not node:
                return 0
            
            # Update the running prefix sum
            current_sum += node.val
            
            # Count how many times (current_sum - targetSum) has appeared
            # This represents valid paths ending at the current node
            path_count = prefix_sums[current_sum - targetSum]
            
            # Add the current prefix sum to the map for child configurations
            prefix_sums[current_sum] += 1
            
            # Recurse down to left and right children
            path_count += dfs(node.left, current_sum)
            path_count += dfs(node.right, current_sum)
            
            # Backtrack: Remove the current prefix sum before moving back up the tree
            prefix_sums[current_sum] -= 1
            
            return path_count
            
        return dfs(root, 0)