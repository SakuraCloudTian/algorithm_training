class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs(r, c, i):
            if i == len(word):  # 找完了
                return True
            if r < 0 or r >= rows or c < 0 or c >= cols:  # 越界
                return False
            if board[r][c] != word[i]:  # 字母不匹配
                return False

            # 标记已经访问，避免重复使用
            temp = board[r][c]
            board[r][c] = '#'

            # 递归查找上下左右
            found = (dfs(r+1, c, i+1) or
                     dfs(r-1, c, i+1) or
                     dfs(r, c+1, i+1) or
                     dfs(r, c-1, i+1))

            board[r][c] = temp  # 回溯恢复原状态
            return found

        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):  # 从任意点出发开始搜索
                    return True
        return False