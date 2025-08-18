class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max=nums[0]
        cur_min=nums[0]
        res=nums[0]
        for i in range(1, len(nums)):
          n=nums[i]
          if n==0:
            res=max(res,0)
            cur_max, cur_min = 0, 0
            continue

          if cur_max == 0 and cur_min == 0:
            cur_max, cur_min = n, n
          else:
              # 遇到负数要交换
              if n < 0:
                  cur_max, cur_min = cur_min, cur_max
              cur_max = max(n, cur_max * n)
              cur_min = min(n, cur_min * n)

          res = max(res, cur_max)

        return res
