"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # 第一步：遍历原链表，保存原节点列表，并构造新节点链表
        old_nodes = []
        new_nodes = []

        curr_old = head
        dummy_head = Node(0)
        curr_new = dummy_head

        while curr_old:
            old_nodes.append(curr_old)
            new_node = Node(curr_old.val)
            new_nodes.append(new_node)
            curr_new.next = new_node
            curr_new = curr_new.next
            curr_old = curr_old.next

        # 第二步：设置新链表中的 random 指针
        for i, old_node in enumerate(old_nodes):
            if old_node.random is not None:
                # 获取 old_node.random 在 old_nodes 中的位置
                random_index = old_nodes.index(old_node.random)
                new_nodes[i].random = new_nodes[random_index]
            else:
                new_nodes[i].random = None

        return dummy_head.next