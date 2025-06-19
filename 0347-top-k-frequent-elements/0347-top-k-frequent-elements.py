class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        num_unique = []
        num_unique_list = []

        # 提取唯一元素
        for num in nums:
            if num not in num_unique:
                num_unique.append(num)

        # 创建频率表
        for num in num_unique:
            num_unique_list.append([num, 0])

        # 统计频率
        for num in nums:
            for item in num_unique_list:
                if item[0] == num:
                    item[1] += 1

        # 冒泡排序（按频率从大到小）
        n = len(num_unique_list)
        for i in range(n-1):
            for j in range(n-1-i):
                if num_unique_list[j][1] < num_unique_list[j+1][1]:
                    num_unique_list[j], num_unique_list[j+1] = num_unique_list[j+1], num_unique_list[j]

        # 返回前k个元素
        return [num_unique_list[i][0] for i in range(k)]
