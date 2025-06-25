# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
    
        nodes = []

        # Step 1: 先序遍历，收集节点
        def preorder(node):
            if node:
                nodes.append(node)
                preorder(node.left)
                preorder(node.right)
        
        preorder(root)

        # Step 2: 重新连接节点
        for i in range(1, len(nodes)):
            prev = nodes[i - 1]
            curr = nodes[i]
            prev.left = None
            prev.right = curr