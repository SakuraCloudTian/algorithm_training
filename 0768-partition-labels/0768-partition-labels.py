class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        # 1. 记录每个字符最后出现的位置
        last = {c: i for i, c in enumerate(s)}
        
        res = []
        start = end = 0
        
        # 2. 一次遍历划分
        for i, c in enumerate(s):
            end = max(end, last[c])
            if i == end:
                res.append(end - start + 1)
                start = i + 1
        
        return res

