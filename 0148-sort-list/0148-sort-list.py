# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 链表为空或只有一个节点时直接返回
        if not head or not head.next:
            return head

        # 找中点并断开链表
        mid = self.getMiddle(head)
        left = head
        right = mid

        # 递归排序左右两部分
        left_sorted = self.sortList(left)
        right_sorted = self.sortList(right)

        # 合并两个有序链表
        return self.merge(left_sorted, right_sorted)

    def getMiddle(self, head: ListNode) -> ListNode:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None  # 断开链表
        return mid

    def merge(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        tail = dummy
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        tail.next = l1 or l2
        return dummy.next
        