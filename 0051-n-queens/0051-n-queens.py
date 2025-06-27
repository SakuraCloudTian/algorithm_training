from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        def is_valid(path, row, col):
            for r in range(row):
                if path[r] == col or abs(path[r] - col) == abs(r - row):
                    return False
            return True

        def dfs(path, row):
            if row == n:
                res.append(path[:])
                return
            for col in range(n):
                if is_valid(path, row, col):
                    dfs(path + [col], row + 1)

        dfs([], 0)

        # 转化为棋盘格式
        result_boards = []
        for solution in res:
            board = []
            for col in solution:
                row_str = ['.'] * n
                row_str[col] = 'Q'
                board.append(''.join(row_str))
            result_boards.append(board)

        return result_boards
