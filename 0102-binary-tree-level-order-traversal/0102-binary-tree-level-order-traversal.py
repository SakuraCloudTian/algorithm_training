# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        def dfs(node, depth):
            if not node:
                return
            # 如果当前深度还没有记录结果，说明当前节点是该层最右边第一个访问到的
            if depth < len(result):
                result[depth].append(node.val)
            if depth == len(result):
                result.append([node.val])
            # 先遍历左子树，再遍历右子树
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)


        dfs(root, 0)
        return result