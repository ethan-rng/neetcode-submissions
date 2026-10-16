# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        p, q = p.val, q.val

        def helper(root, p, q):
            left, right = root.left, root.right
            if (p < root.val and q > root.val) or (p > root.val and q < root.val) or p == root.val or q == root.val:
                return root


            if p < root.val and q < root.val:
                return helper(root.left, p, q)
            elif p > root.val and q > root.val:
                return helper(root.right, p, q) 
           
            
        return helper(root, p, q)
            

