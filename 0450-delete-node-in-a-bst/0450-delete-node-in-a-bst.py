# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        # 1. Search for the node
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # 2. Node found, handle deletion
            # Case: Leaf or only one child
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            
            # Case: Two children
            # Find the in-order successor (smallest in the right subtree)
            successor = root.right
            while successor.left:
                successor = successor.left
            
            # Replace current node value with successor value
            root.val = successor.val
            # Delete the successor node
            root.right = self.deleteNode(root.right, successor.val)
            
        return root