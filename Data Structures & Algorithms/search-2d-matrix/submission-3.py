class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        left = 0
        right = (rows * cols) - 1

        while left <= right:
            m = left + ((right - left)// 2)
            mval = matrix[m // cols][m % cols]

            if mval == target:
                return True
            elif mval < target:
                left = m + 1
            else:
                right = m - 1

        return False       