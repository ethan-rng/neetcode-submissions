# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        
        queue = deque([root])
        depth = 0
 
        while queue:
            currLength = len(queue)

            for _ in range(currLength):
                currNode = queue.popleft()

                if currNode and currNode.left:
                    queue.append(currNode.left)
                if currNode and currNode.right:
                    queue.append(currNode.right)
            
            depth += 1
        
        return depth