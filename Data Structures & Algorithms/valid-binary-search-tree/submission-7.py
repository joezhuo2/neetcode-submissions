# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node: Optional[TreeNode], high: float, low: float) -> bool:
            if not node:
                return True
            
            if not (low < node.val < high):
                return False
            
            return validate(node.left, node.val, low) and validate(node.right, high, node.val)
 
        return validate(root, float('inf'), float('-inf'))