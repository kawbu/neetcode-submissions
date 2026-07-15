class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # search to find correct row:
        l, r = 0, len(matrix) - 1
        midRow = 0
        while l <= r:
            midRow = (l + r) // 2
            lVal, rVal = matrix[midRow][0], matrix[midRow][-1]
            #check if value in current
            if target >= lVal and target <= rVal:
                break
            if target < lVal:
                r = midRow - 1
            else:
                l = midRow + 1
        # now find correct item in the row (basic binary search)
        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            midCol = (l + r) // 2
            lVal, rVal = matrix[midRow][midCol], matrix[midRow][midCol]
            #check if value in current
            if target < lVal:
                r = midCol - 1
            elif target > rVal:
                l = midCol + 1
            else:
                return True
        return False
