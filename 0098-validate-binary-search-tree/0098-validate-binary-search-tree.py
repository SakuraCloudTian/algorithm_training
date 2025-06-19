# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node, low=float('-inf'), high=float('inf')):
            if not node:
                return True
            if not (low < node.val < high):
                return False
            # 左子树最大不能超过当前值，右子树最小不能小于当前值
            return helper(node.left, low, node.val) and helper(node.right, node.val, high)
        
        return helper(root)
