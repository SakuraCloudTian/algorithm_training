from collections import Counter, defaultdict
class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        # 1. 全局统计每个字母的出现总次数
        total = Counter(s)
        
        res = []
        n = len(s)
        start = 0
        
        # 2. 从 start 开始，构造每个待定列表（segment）
        while start < n:
            seen = defaultdict(int)  # 当前 segment 内各字母的计数
            chars = set()            # 当前 segment 包含的字母集合
            end = start              # 区间右端指针
            
            # 不断尝试扩张区间
            while end < n:
                c = s[end]
                seen[c] += 1
                chars.add(c)
                
                # 检查当前 segment 内所有字母是否都已达到全局出现次数
                complete = True
                for ch in chars:
                    if seen[ch] < total[ch]:
                        complete = False
                        break
                
                # 如果都“集齐”了，就可以切分
                if complete:
                    break
                end += 1
            
            # 记录这个 segment 的长度，并从下一个位置重新开始
            res.append(end - start + 1)
            start = end + 1
        
        return res

