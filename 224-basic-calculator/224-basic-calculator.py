class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        res, cur_num, sign = 0, 0, 1
        stack = []
        for i in range(len(s)):
            char = s[i]
            if char.isdigit():
                cur_num = cur_num*10 + int(char)
            if (not char.isdigit() and char != ' ') or i == len(s)-1:
                if char == '+':
                    res += sign*cur_num
                    cur_num = 0
                    sign = 1
                elif char == '-':
                    res += sign*cur_num
                    cur_num = 0
                    sign = -1
                elif char == '(':
                    stack.append(res)
                    stack.append(sign)
                    res = 0
                    sign = 1
                elif char == ')':
                    res += sign*cur_num
                    res = res*stack.pop() + stack.pop()
                    cur_num = 0
        res += sign*cur_num
        return res