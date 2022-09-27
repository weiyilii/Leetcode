class Solution:
    def calculate(self, s: str) -> int:
        res, num, sign = 0, 0, 1
        stack = []
        for c in s:
            if c.isdigit():
                num = num*10 + int(c)
            elif c == "+":
                res += num*sign
                num, sign = 0, 1
            elif c == "-":
                res += num*sign
                num, sign = 0, -1
            elif c == "(":
                stack.append(res)
                stack.append(sign)
                res = 0
                num, sign = 0, 1
            elif c == ")":
                res += num*sign
                res = res*stack.pop()
                res += stack.pop()
                num, sign = 0, 1
        
        return res + num*sign