# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val: i for i, val in enumerate(inorder)}
        preorder_i = 0

        def helper(l: int, r: int) -> TreeNode | None:
            nonlocal preorder_i
            
            if l > r:
                return None
            root_val = preorder[preorder_i]
            root = TreeNode(root_val)

            preorder_i += 1

            m = inorder_map[root_val]

            root.left = helper(l, m - 1)
            root.right = helper(m+1, r)

            return root

        return helper(0, len(inorder) - 1)