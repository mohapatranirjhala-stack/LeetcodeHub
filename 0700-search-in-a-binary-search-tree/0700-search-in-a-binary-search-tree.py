# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        current = root
        
        # Traverse the tree based on BST properties
        while current is not None:
            if current.val == val:
                return current
            elif val < current.val:
                current = current.left
            else:
                current = current.right
                
        # If the value is not found in the BST
        return None