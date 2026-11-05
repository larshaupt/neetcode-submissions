class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ["+", "-", "*", "/"]
        stack = []
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                val1 = stack.pop()
                val2 = stack.pop()
                if token == "+":
                    res = val1 + val2
                elif token == "-":
                    res = val2 - val1
                elif token == "*":
                    res = val1 * val2
                elif token == "/":
                    res = int(val2/val1)
                stack.append(res)
        return int(stack[-1])