import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        left = 1
        for i in range(1, n):
            prod = left * nums[i-1]
            res[i] = prod
            left = prod

        
        right = 1
        for i in range(n-2, -1, -1):
            prod = right * nums[i+1]
            res[i] = res[i] * prod
            right = prod 
        return res
            
