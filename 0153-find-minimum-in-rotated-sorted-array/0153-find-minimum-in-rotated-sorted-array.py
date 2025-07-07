class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        # 如果数组已经是升序（没有旋转）
        if nums[left] < nums[right]:
            return nums[left]

        while left < right:
            mid = (left + right) // 2

            # 最小值一定在 mid 右侧
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                # 最小值在左边或是 mid 本身
                right = mid

        return nums[left]