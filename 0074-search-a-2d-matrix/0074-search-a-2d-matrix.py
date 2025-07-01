class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #获取行和列
        rows=len(matrix)
        cols=len(matrix[0])
        res=False
        def bf_rows(m,n,target):
            begin,end=m,n-1
            ans=-1
            while begin <= end:
                mid = (begin + end) // 2
                if matrix[mid][0] <= target:
                    ans = mid      # 当前这一行可能包含 target
                    begin = mid + 1
                else:
                    end = mid - 1
            return ans

        def bf_cols(m,n,target):
            begin,end=0,n-1
            while begin<=end:
                mid=(begin+end)//2
                if target < matrix[m][mid]:
                    end = mid-1
                elif target>matrix[m][mid]:
                    begin =mid+1
                else:
                    return True
            return False

        if target >= matrix[0][0] and target <= matrix[rows-1][cols-1]:
            target_row=bf_rows(0,rows,target)
            res=bf_cols(target_row,cols,target)
        else:
            res=False
        return res