class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left_i, right_i = 0, n-1

        while left_i <= right_i:
            center = (left_i + right_i)//2
            center_val = nums[center]
            if center_val == target:
                return center
            if center_val > target:
                # must be on left side
                right_i = center-1
            else:
                left_i = center+1
            
        return -1