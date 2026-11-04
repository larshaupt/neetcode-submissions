class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        max_length = 1
        left_i, right_i = 0,1
        substring_chars = set([s[0]])
        while right_i < len(s):
            if s[right_i] in substring_chars:
                # remove chars from the left until duplicate char is removed
                while s[left_i] != s[right_i] and left_i < right_i:
                    substring_chars.remove(s[left_i])
                    left_i += 1
                substring_chars.remove(s[left_i])
                left_i += 1
            else:
                substring_chars.add(s[right_i])
                max_length = max(max_length, right_i + 1 - left_i)
                right_i += 1
        return max_length


        