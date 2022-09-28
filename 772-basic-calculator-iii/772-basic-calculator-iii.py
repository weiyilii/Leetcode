class Solution:
    def calculate(self, s: str) -> int:
        
        def helper(s):
            stack = []
            num, op = 0, "+"
            
            while len(s) > 0:
                c = s.popleft()
                if c.isdigit():
                    num = num*10 + int(c)
                    
                if c == "(":
                    num = helper(s)
                    
                if (not c.isdigit() and c != " ") or len(s) == 0:
                    if op == "+":
                        stack.append(num)
                    if op == "-":
                        stack.append(-num)
                    if op == "*":
                        stack[-1] = stack[-1]*num
                    if op == "/":
                        stack[-1] = int(float(stack[-1])/num)
                    num, op = 0, c
                
                if c == ")":
                    break
            return sum(stack)
        
        return helper(collections.deque(s))