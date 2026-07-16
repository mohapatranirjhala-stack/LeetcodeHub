# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def get_leaves(root: Optional[TreeNode], leaf_list: list[int]):
            if not root:
                return
            
            # Check if the current node is a leaf node
            if not root.left and not root.right:
                leaf_list.append(root.val)
                return
            
            # Recurse on left and right subtrees
            get_leaves(root.left, leaf_list)
            get_leaves(root.right, leaf_list)
            
        leaves1 = []
        leaves2 = []
        
        # Collect leaf sequences for both trees
        get_leaves(root1, leaves1)
        get_leaves(root2, leaves2)
        
        # Return True if the sequences are identical, False otherwise
        return leaves1 == leaves2