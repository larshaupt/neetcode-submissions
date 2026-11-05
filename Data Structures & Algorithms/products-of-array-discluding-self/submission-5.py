import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        last_right_prod = 1
        last_left_prod = 1
        left_prods, right_prods = [last_left_prod], [last_right_prod]
        for i in range(len(nums)):
            new_left_prod = last_left_prod * nums[i]
            new_right_prod = last_right_prod * nums[-i-1]
            left_prods.append(new_left_prod)
            right_prods.append(new_right_prod)
            last_left_prod = new_left_prod
            last_right_prod = new_right_prod
        
        prods = []
        #print(left_prods, right_prods)
        for i in range(len(nums)):
            prods.append(left_prods[i] * right_prods[len(nums)-i-1])
        return prods
            