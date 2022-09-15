class Solution:
    def calculate(self, s: str) -> int:
        res, number, sign = 0, 0, 1
        stack = []
        for i in range(len(s)):
            c = s[i]
            if c.isdigit():
                number = number*10 + int(c)
            if c == "+":
                res += number*sign
                number, sign = 0, 1
            if c == "-":
                res += number*sign
                number, sign = 0, -1
            if c == "(":
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            if c == ")":
                res += number*sign
                res = res*stack.pop() + stack.pop()
                number = 0
        res += number*sign
        return res