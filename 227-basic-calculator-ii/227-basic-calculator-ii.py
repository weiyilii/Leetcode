class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        res, cur_num, last_num, op = 0, 0, 0, '+'
        for i in range(len(s)):
            char = s[i]
            if char.isdigit():
                cur_num = cur_num*10 + int(char)
            if (not char.isdigit() and char != ' ') or i == len(s)-1:
                if op == '+':
                    res += last_num
                    last_num = cur_num
                elif op == '-':
                    res += last_num
                    last_num = -cur_num
                elif op == '*':
                    last_num = last_num*cur_num
                elif op == '/':
                    last_num = int(float(last_num)/cur_num)
                op = char
                cur_num = 0
        res += last_num
        return res