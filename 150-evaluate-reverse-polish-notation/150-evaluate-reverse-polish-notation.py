class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for op in tokens:
            if op not in ("+", "-", "*", "/"):
                stack.append(int(op))
            else:
                n1 = stack.pop()
                n2 = stack.pop()
                if op == "+":
                    stack.append(n1 + n2)
                if op == "-":
                    stack.append(n2 - n1)
                if op == "*":
                    stack.append(n1*n2)
                if op == "/":
                    stack.append(int(n2/n1))
        return stack[0]