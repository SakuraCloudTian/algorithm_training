class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)
        if n < 3:
            return 0
        
        result = 0
        i = 0

        # 前缀和预处理
        prefix_sum = [0] * (n + 1)
        for idx in range(n):
            prefix_sum[idx + 1] = prefix_sum[idx] + height[idx]

        # 后缀最大值索引预处理
        right_max_pos = [0] * n
        max_pos = n - 1
        for idx in reversed(range(n)):
            if height[idx] > height[max_pos]:
                max_pos = idx
            right_max_pos[idx] = max_pos

        while i < n - 1:
            if height[i + 1] >= height[i]:
                i += 1
                continue

            j = i + 1
            # 查找终点（第一个 ≥ 起点的 或者右边最大点）
            boundary = -1
            for k in range(j, n):
                if height[k] >= height[i]:
                    boundary = k
                    break
            if boundary == -1:
                boundary = right_max_pos[i + 1]

            water_level = min(height[i], height[boundary])
            width = boundary - i - 1
            if width > 0:
                sum_between = prefix_sum[boundary] - prefix_sum[i + 1]
                water = water_level * width - sum_between
                result += water

            i = boundary

        return result
