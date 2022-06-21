class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        ops = {"+", "-", "*", "/"}
        
        for i in tokens:
            if i not in ops:
                stack.append(int(i))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                if i == "+":
                    num = num1 + num2
                elif i == "-":
                    num = num1 - num2
                elif i == "*":
                    num = num1 * num2
                else:
                    num = int(float(num1) / num2)
                stack.append(num)
        
        return stack[0]
            