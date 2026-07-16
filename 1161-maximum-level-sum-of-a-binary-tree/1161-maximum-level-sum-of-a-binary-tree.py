# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        # Initialize max_sum to -infinity to safely handle negative node values
        max_sum = float('-inf')
        max_level = 1
        current_level = 1
        
        queue = deque([root])
        
        while queue:
            level_sum = 0
            level_length = len(queue)
            
            # Process all nodes belonging to the current level
            for _ in range(level_length):
                node = queue.popleft()
                level_sum += node.val
                
                # Enqueue children for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Update max tracking variables if a strictly larger sum is found
            if level_sum > max_sum:
                max_sum = level_sum
                max_level = current_level
            
            # Move to the next depth level
            current_level += 1
            
        return max_level