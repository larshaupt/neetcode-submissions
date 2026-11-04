class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        triplets = []

        i = 0
        while i < len(nums):
            num = nums[i]
            left_i, right_i = i+1, len(nums)-1
            while left_i < right_i:
                left_val, right_val = nums[left_i], nums[right_i]
                num_sum = left_val + right_val
                if num_sum == -num:
                    triplets.append([left_val, right_val, num])
                    while left_i < right_i and nums[left_i] == left_val:
                        left_i += 1
                elif num_sum > -num:
                    right_i = right_i - 1
                else:
                    left_i = left_i + 1
            while i < len(nums) and nums[i] == num:
                i+=1

        return triplets