# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.res=0
        def check_sum_value(sum_val):
            global res
            for i in range(len(sum_val)):
                value = sum(sum_val[i:])
                if value == targetSum:
                    self.res += 1

        def dfs(root, sum_val):
            global res
            if not root:
                return
            sum_val.append(root.val)
            check_sum_value(sum_val)
            if root.left:
                dfs(root.left, sum_val)
            if root.right:
                dfs(root.right, sum_val)
            sum_val.pop()  # 回溯
        
        dfs(root,[])
        return self.res