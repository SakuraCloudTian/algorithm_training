class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A  # 保证 A 是较短的数组

        m, n = len(A), len(B)
        total = m + n
        half = total // 2

        l, r = 0, m
        while l <= r:
            i = (l + r) // 2  # A中的切分点
            j = half - i      # B中的切分点

            Aleft = A[i - 1] if i > 0 else float('-inf')
            Aright = A[i] if i < m else float('inf')
            Bleft = B[j - 1] if j > 0 else float('-inf')
            Bright = B[j] if j < n else float('inf')

            # 满足中位数条件
            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:  # 奇数
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1

        