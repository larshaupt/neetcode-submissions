from collections import defaultdict
class Solution:
    def trap(self, height: List[int]) -> int:
        width = len(height)
        highest_from_left, highest_from_right = [], []
        highest_left, highest_right = 0,0
        for i in range(width):
            highest_left = max(highest_left, height[i])
            highest_from_left.append(highest_left)
            highest_right = max(highest_right, height[-i-1])
            highest_from_right.append(highest_right)
        total_vol = 0
        for i in range(1, width-1): #skip borders
            lowest_sides = min(highest_from_left[i-1], highest_from_right[width - 2 - i])
            total_vol += max(0, lowest_sides - height[i])

        return total_vol
            
                
