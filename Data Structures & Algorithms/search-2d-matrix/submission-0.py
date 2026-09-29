class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m * n - 1
        while l <= r:
            M = l + (r-l)//2
            mid = matrix[M//n][M%n]
            if mid == target:
                return True
            elif mid > target:
                r = M - 1
            else:
                l = M + 1
        return False