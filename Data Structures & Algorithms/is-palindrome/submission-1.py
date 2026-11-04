class Solution:
    def isPalindrome(self, s: str) -> bool:
        def is_alnum(c):
            o = ord(c)
            return (ord("0") <= o <= ord("9") or
                    ord("a") <= o <= ord("z"))


        s = [char.lower() for char in s if is_alnum(char.lower())]
        i, j = 0, len(s)-1
        while j >= i+1:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True