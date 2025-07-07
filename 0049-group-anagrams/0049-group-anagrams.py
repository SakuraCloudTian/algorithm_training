class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_table = defaultdict(list)
        
        for word in strs:
            key = ''.join(sorted(word))  # 排序后的字符串作为 key
            hash_table[key].append(word)

        return list(hash_table.values())  # 返回所有分组