class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left_i, right_i = 0, len(numbers) - 1
        while left_i < right_i:
            
            num_sum = numbers[left_i] + numbers[right_i]
            if num_sum == target:
                return [left_i+1, right_i+1]
            
            if num_sum - target > 0:
                right_i -= 1
            else:
                left_i += 1

