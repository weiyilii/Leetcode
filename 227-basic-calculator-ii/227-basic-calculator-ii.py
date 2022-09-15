class Solution:
    def calculate(self, s: str) -> int:
        number, op = 0, "+"
        stack = []
        for i in range(len(s)):
            c = s[i]
            if c.isdigit():
                number = number*10 + int(c)
            if c in ("+", "-", "*", "/"):
                if op == "+":
                    stack.append(number)
                if op == "-":
                    stack.append(-number)
                if op == "*":
                    n = stack.pop()
                    stack.append(n*number)
                if op == "/":
                    n = stack.pop()
                    stack.append(int(n/number))
                number = 0
                op = c
        if op == "+":
            stack.append(number)
        if op == "-":
            stack.append(-number)
        if op == "*":
            n = stack.pop()
            stack.append(n*number)
        if op == "/":
            n = stack.pop()
            stack.append(int(n/number)) 
        
        return sum(stack)