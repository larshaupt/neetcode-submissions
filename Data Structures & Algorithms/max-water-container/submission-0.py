class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        left_i, right_i = 0, n-1
        max_vol = 0
        while left_i < right_i:
            left_val, right_val = heights[left_i], heights[right_i]
            vol = (right_i - left_i) * min(left_val, right_val)
            max_vol = max(max_vol, vol)
            if left_val > right_val:
                right_i -= 1
            else:
                left_i += 1
        return max_vol

        