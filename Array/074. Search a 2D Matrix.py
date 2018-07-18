"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:
Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
"""

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        
        nrow = len(matrix)
        ncol = len(matrix[0])

        low, high = 0, nrow * ncol - 1
        while low <= high:
            mid = (low + high) / 2
            if matrix[mid// ncol][mid % ncol] == target:
                return True
            elif matrix[mid//ncol][mid % ncol] < target:
                low = mid + 1
            else:
                high = mid - 1
        return False



if __name__ == "__main__":
    print Solution().searchMatrix( [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
], 7)


        
