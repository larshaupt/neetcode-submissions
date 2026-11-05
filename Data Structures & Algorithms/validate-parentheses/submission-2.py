class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        if len(s)%2 != 0:
            return False

        pairs = ["()", "[]", "{}"]
    
        stack = []
        for char in s:
            if char in [p[1] for p in pairs]:
                #closing, need to be the last element on the stack
                if not stack:
                    return False
                last_element = stack.pop()
                for p in pairs:
                    if last_element == p[0] and char != p[1]:
                        return False
            else:
                stack.append(char)
        return not stack