
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        open_temps_stack = []
        for i, temp in enumerate(temperatures):
            while open_temps_stack and temperatures[open_temps_stack[-1]] < temp:
                # found the warmer temp
                res[open_temps_stack[-1]] = i - open_temps_stack[-1]
                open_temps_stack.pop()
            open_temps_stack.append(i)
        return res


