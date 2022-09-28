class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num, op = 0, "+"
        
        def compute(num, op):
            if op == "+":
                stack.append(num)
            elif op == "-":
                stack.append(-num)
            elif op == "*":
                prev = stack.pop()
                stack.append(prev*num)
            elif op == "/":
                prev = stack.pop()
                stack.append(int(float(prev)/num))
        
        for i in range(len(s)):
            print(stack)
            c = s[i]
            if c.isdigit():
                num = num*10 + int(c)
            if c in ("+", "-", "*", "/"):
                compute(num, op)
                num, op = 0, c
            if c == "(":
                #stack.append(num)
                stack.append(op)
                num, op = 0, "+"
            if c == ")":
                compute(num, op)
                num = 0
                while stack and stack[-1] not in ("+", "-", "*", "/"):
                    num += stack.pop()
                if stack:
                    op = stack.pop()
                    compute(num, op)
                    num, op = 0, c
        compute(num, op)
        return sum(stack)
                