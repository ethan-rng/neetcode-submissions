class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:  
        inf = float('inf')
    
        def dfs(root: Optional[TreeNode], minVal: int, maxVal: int):
            # Base Conditions  
            if not root:
                return True

            if not root.left and not root.right:
                return True
            
            val = root.val

            # CHANGED: left child must be less than val (was maxVal)
            if root.left and not (root.left.val < val and root.left.val > minVal):
                return False

            # CHANGED: right child must be greater than val (was minVal)
            if root.right and not (root.right.val < maxVal and root.right.val > val):
                return False

            # Recursion
            if root.left and not dfs(root.left, minVal, val):
                return False
            if root.right and not dfs(root.right, val, maxVal):
                return False

            return True
        
        return dfs(root, -inf, inf)