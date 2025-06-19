class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]  # 回文子串

        res = ""
        for i in range(len(s)):
            # 奇数回文
            tmp1 = expand(i, i)
            # 偶数回文
            tmp2 = expand(i, i + 1)
            if len(tmp1) > len(res):
                res = tmp1
            if len(tmp2) > len(res):
                res = tmp2
        return res
