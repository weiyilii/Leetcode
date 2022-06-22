class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        number, op = 0, '+'
        for i in range(len(s)):
            char = s[i]
            if char.isdigit():
                number = number*10 + int(char)
            if (not char.isdigit() and char != ' ') or i == len(s)-1:
                if op == '+':
                    stack.append(number)
                elif op == '-':
                    stack.append(-number)
                elif op == '*':
                    stack.append(stack.pop()*number)
                elif op == '/':
                    stack.append(int(float(stack.pop())/number))
                op = char
                number = 0
        return sum(stack)