class Solution:
    def calculate(self, s: str) -> int:
        stack = [0]
        num, op = 0, "+"
        for c in s:
            if c.isdigit():
                num = num*10 + int(c)
            elif c in ("+", "-", "*", "/"):
                if op == "*":
                    prev = stack.pop()
                    new = prev*num
                    stack.append(new)
                elif op == "/":
                    prev = stack.pop()
                    new = int(prev/num)
                    stack.append(new)
                elif op == "+":
                    stack.append(num)
                elif op == "-":
                    stack.append(-num)
                num, op = 0, c
                
        if op == "*":
            prev = stack.pop()
            new = prev*num
            stack.append(new)
        elif op == "/":
            prev = stack.pop()
            new = int(prev/num)
            stack.append(new)
        elif op == "+":
            stack.append(num)
        elif op == "-":
            stack.append(-num)
        return sum(stack)