from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0
        max_len = 1
        nums = set(nums)
        for num in nums:
            if num - 1 in nums:
                continue
            length = 1
            i = 1
            while num+i in nums:
                i += 1
                length += 1
            max_len = max(max_len, length)
        return max_len