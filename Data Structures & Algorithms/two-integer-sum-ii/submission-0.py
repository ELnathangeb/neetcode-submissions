class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            cuurent_sum = numbers[left] + numbers[right]
            if cuurent_sum == target:
                return [left + 1, right + 1]
            elif cuurent_sum < target:
                left += 1
            else:
                right -= 1

        return []
        


        