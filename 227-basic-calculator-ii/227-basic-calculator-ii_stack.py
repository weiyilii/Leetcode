class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        # number is the newest number that has not been appended to stack or calculated
        # op is the last operation we've seen
        number, op = 0, '+'
        for i in range(len(s)):
            char = s[i]
            if char.isdigit():
                number = number*10 + int(char)
            # if current char is operation, we need to evaluate last operation
            if (not char.isdigit() and char != ' ') or i == len(s)-1:
                # if last op is + or -, no need to calculate for now, just append newest number
                if op == '+':
                    stack.append(number)
                elif op == '-':
                    stack.append(-number)
                # if last op is *, calculate using stack.pop() and current number, then append it to stack
                elif op == '*':
                    num1 = stack.pop()
                    stack.append(num1*number)
                elif op == '/':
                    num1 = stack.pop()
                    stack.append(int(float(num1)/number))
                op = char
                number = 0
                
        return sum(stack)     
