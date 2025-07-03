# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy

        while True:
            min_index = -1
            min_value = float('inf')

            # 同时获取每个链表的头节点，并找到最小值
            for i in range(len(lists)):
                if lists[i] and lists[i].val < min_value:
                    min_value = lists[i].val
                    min_index = i

            # 如果没有找到最小值（说明所有链表都遍历完了），退出循环
            if min_index == -1:
                break

            # 把找到的最小节点加入结果链表
            current.next = lists[min_index]
            current = current.next

            # 更新这个链表的头指针
            lists[min_index] = lists[min_index].next

        return dummy.next