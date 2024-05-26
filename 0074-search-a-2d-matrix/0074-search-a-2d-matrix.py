class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        m, n = len(matrix), len(matrix[0])
        l,r = 0, m*n-1
        while l <= r:
            m = (l+r)//2
            ro,c = m//n, m%n
            v = matrix[ro][c]
            if v == target:
                return True
            elif v < target:
                l = m + 1
            else:
                r = m - 1
        return False