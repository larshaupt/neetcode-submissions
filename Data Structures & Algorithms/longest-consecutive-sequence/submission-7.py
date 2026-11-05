from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) < 1:
            return 0
        max_nums = max(nums)
        max_len = 1
        sequences = {}
        for num in nums:
            sequences[num] = 1
            if num-1 in sequences:
                # number before already exists here
                sequences[num] = sequences[num-1] + sequences[num]
                max_len = max(max_len, sequences[num])
            i = 1
            while num+i in sequences and num+i <= max_nums:
                #print("exists", num+i)
                # number after alredy exists
                sequences[num+i] = sequences[num] + i
                max_len = max(max_len, sequences[num] + i)
                i += 1
            #print(num, max_len, dict(sequences))
        return max_len

        
        

        