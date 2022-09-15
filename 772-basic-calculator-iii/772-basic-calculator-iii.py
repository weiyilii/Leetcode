class Solution:    
    def calculate(self, s: str) -> int:
        stack = []
        num, op = 0, "+"
        
        def update(op, num):
            if op == "+":
                stack.append(num)
            if op == "-":
                stack.append(-num)
            if op == "*":
                stack.append(stack.pop()*num)
            if op == "/":
                stack.append(int(stack.pop()/num))
        
        for c in s:
            #print(stack, op, num)
            if c.isdigit():
                num = num*10 + int(c)
            if c in ("+", "-", "*", "/"):
                update(op, num)
                op, num = c, 0
            if c == "(":
                stack.append(op)
                op = "+"
            if c == ")":
                update(op, num)
                print(stack)
                num = 0
                while stack[-1] not in ("+", "-", "*", "/"):
                    num += stack.pop()
                update(stack.pop(), num)
                op, num = c, 0
        update(op, num)
        return sum(stack)