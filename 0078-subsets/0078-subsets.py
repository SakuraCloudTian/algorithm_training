class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for num in nums:
            # 对当前结果中的每个子集加上新元素 num，生成新的子集
            new_subsets = [curr + [num] for curr in result]
            result.extend(new_subsets)
        return result
