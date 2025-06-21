# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 按照你的思路，用一个初始节点 res_list 来串起所有新节点
        dummy    = ListNode(0)  # 虚拟头节点，不存实际数据
        tail     = dummy        # tail 始终指向结果链表的最后一个节点
        carry    = 0            # 进位

        # 当 l1、l2 还有节点，或者最后还有进位时，都要继续
        while l1 is not None or l2 is not None or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            s  = v1 + v2 + carry

            carry     = s // 10
            new_digit = s % 10

            # 创建新节点，接到 tail 后面
            tail.next = ListNode(new_digit)
            tail      = tail.next

            # 推进 l1 和 l2
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        # 结果链表的真正头是 dummy.next
        res_list = dummy.next
        return res_list

                