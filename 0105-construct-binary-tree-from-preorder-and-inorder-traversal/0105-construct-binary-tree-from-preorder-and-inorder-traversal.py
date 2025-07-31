# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        # 构建值到索引的映射表（加速查找）
        inorder_index_map = {value: idx for idx, value in enumerate(inorder)}

        # 前序索引指针
        self.pre_idx = 0

        def helper(in_left, in_right):
            if in_left > in_right:
                return None
            
            # 从前序中取出当前根节点的值
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)

            # 分割中序数组
            index = inorder_index_map[root_val]
            root.left = helper(in_left, index - 1)
            root.right = helper(index + 1, in_right)
            return root

        return helper(0, len(inorder) - 1)