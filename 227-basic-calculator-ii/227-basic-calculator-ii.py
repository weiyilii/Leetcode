class Solution:
    def calculate(self, s: str) -> int:
        stack = [0]
        num, op = 0, "+"
        for i in range(len(s)):
            #print(stack)
            c = s[i]
            if c.isdigit():
                num = num*10 + int(c)
            if c in ("+", "-", "*", "/") or i == len(s)-1:
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
        return sum(stack)