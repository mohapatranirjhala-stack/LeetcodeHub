# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # Base Cases: if we reach the end of a branch or find either target node
        if root is None or root == p or root == q:
            return root
            
        # Recurse on left and right subtrees
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # If p and q are found in different subtrees, current root is the LCA
        if left is not None and right is not None:
            return root
            
        # Otherwise, return the non-null result (whichever subtree contains the targets)
        return left if left is not None else right