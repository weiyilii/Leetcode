class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        res, last = 0, 0
        number, op = 0, '+'
        for i in range(len(s)):
            char = s[i]
            if char.isdigit():
                number = number*10 + int(char)
            if (not char.isdigit() and char != ' ') or i == len(s)-1:
                if op == '+':
                    res += last
                    last = number
                elif op == '-':
                    res += last
                    last = -number
                elif op == '*':
                    last = last*number
                elif op == '/':
                    last = int(float(last)/number)
                op = char
                number = 0
        res += last
        
        return res   