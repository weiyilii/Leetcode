class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        # res: calculated from previous expressions
        # number: newest number that is going to be operated
        # sign: only +1 or -1 to decide plus or minus number
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
            # if meet (, append previous result and sign into stack, sign on top, redo a new calculation
            elif char == '(':
                stack.append(res)
                stack.append(sign)
                res, sign = 0, 1
            # if ), current res + sign*num is the result inside parenthese
            # 1st stack.pop() gives sign of it, 2st stack.pop() gives old result
            elif char == ')':
                res += number*sign
                res = res*stack.pop() + stack.pop()
                number = 0
        res += number*sign
        return res
