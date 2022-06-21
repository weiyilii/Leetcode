class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        res, number, sign = 0, 0, 1
        stack = []
        for i in range(len(s)):
            char = s[i]
            if char.isdigit():
                number = number*10 + int(char)
            elif char == '+':
                res += number*sign
                number = 0
                sign = 1
            elif char == '-':
                res += number*sign
                number = 0
                sign = -1
            elif char == '(':
                stack.append(res)
                stack.append(sign)
                res, sign = 0, 1
            elif char == ')':
                res += number*sign
                res = res*stack.pop() + stack.pop()
                number = 0
        res += number*sign
        return res