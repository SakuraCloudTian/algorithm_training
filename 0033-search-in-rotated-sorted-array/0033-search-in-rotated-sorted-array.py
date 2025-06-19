from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def check_list(list_checked):
            change_point = 0
            total_offset = 0

            while True:
                list_len = len(list_checked)
                if list_len < 2:
                    return 0

                check_point = list_len // 2
                list_cut_point_before = list_checked[check_point - 1]
                list_cut_point_after = list_checked[check_point]

                if list_cut_point_before > list_cut_point_after:
                    change_point = check_point
                    break

                if list_checked[0] <= list_cut_point_before:
                    list_checked = list_checked[check_point:]
                    total_offset += check_point
                else:
                    list_checked = list_checked[:check_point]

            return total_offset + change_point

        def binary_search_range(arr, target, left, right):
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] == target:
                    return mid
                elif arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1

        if not nums:
            return -1
        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        check_point = check_list(nums)

        if nums[check_point] <= target <= nums[-1]:
            # 在右半段查找
            return binary_search_range(nums, target, check_point, len(nums) - 1)
        else:
            # 在左半段查找
            return binary_search_range(nums, target, 0, check_point - 1)
