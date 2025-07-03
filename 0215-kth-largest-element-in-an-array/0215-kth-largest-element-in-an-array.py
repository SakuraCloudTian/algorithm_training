import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 初始化最小堆
        min_heap = nums[:k]
        heapq.heapify(min_heap)

        # 遍历剩余元素
        for num in nums[k:]:
            if num > min_heap[0]:  # 如果比堆顶大
                heapq.heappop(min_heap)  # 弹出堆顶
                heapq.heappush(min_heap, num)  # 加入新元素

        return min_heap[0]  # 堆顶是第k大
        