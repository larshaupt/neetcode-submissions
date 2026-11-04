class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        missing_num = {}

        for i, num in enumerate(numbers):
            if num in missing_num:
                return [missing_num[num]+1, i+1]
            else:
                missing_num[target-num] = i