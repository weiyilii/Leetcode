class Solution:
    def calculate(self, s: str) -> int:
        res, number, sign = 0, 0, 1
        i = 0
        stack = []
        while i < len(s):
            c = s[i]
            if c.isdigit():
                number = number*10 + int(s[i])
            if c == "+":
                res += number*sign
                number = 0
                sign = 1
            if c == "-":
                res += number*sign
                number = 0
                sign = -1
            elif c == "(":
                stack.append(res)
                stack.append(sign)
                sign = 1
                res = 0
            elif c == ")":
                res += number*sign
                res = res*stack.pop() + stack.pop()
                number = 0
            i += 1
        res += number*sign
        return res
            