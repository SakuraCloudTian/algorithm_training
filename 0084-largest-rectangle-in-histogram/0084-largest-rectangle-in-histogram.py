class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        n = len(heights)
        if n == 0:
            return 0

        left = [0] * n
        right = [n] * n  # 初始化为 n 表示到最右边界

        stack = []

        # 从左往右，计算每个位置左边第一个比它小的位置
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)

        stack = []

        # 从右往左，计算每个位置右边第一个比它小的位置
        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            right[i] = stack[-1] if stack else n
            stack.append(i)

        # 计算每个位置作为高时的最大面积
        max_area = 0
        for i in range(n):
            width = right[i] - left[i] - 1
            max_area = max(max_area, heights[i] * width)

        return max_area
