class Solution:
    def partition(self, s: str) -> list[list[str]]:
        res = []

        # 判断是否为回文串
        def check_site(a, b, str_):
            if a >= b:
                return True
            if str_[a] != str_[b]:
                return False
            return check_site(a + 1, b - 1, str_)

        # 回溯函数
        def backtrack(start, path):
            if start == len(s):
                res.append(path[:])
                return
            for end in range(start, len(s)):
                substr = s[start:end+1]
                if check_site(0, len(substr)-1, substr):
                    path.append(substr)
                    backtrack(end + 1, path)
                    path.pop()

        backtrack(0, [])
        return res
