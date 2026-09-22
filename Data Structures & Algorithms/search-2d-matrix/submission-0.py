class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            for j in matrix[i]:
                if j == target:
                    return True
        return False


        '''
        left = 0
        right = len(matrix) * len(matrix[0]) - 1

        while left <= right:
            row = mid // len(matrix[0])
            col = mid % len(matrix[0])

            if matrix[row][col] == target:
                return mid
            elif matrix[row][col] > target:
                right = 

        
           if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid -1
            elif nums[mid] < target:
                left = mid + 1

        '''