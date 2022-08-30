class Solution(object):
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        last_n, last_d, sign = 0, 1, 1
        i = 0
        while i < len(expression):
            c = expression[i]
            if c == "-":
                sign = -1
            elif c == "+":
                sign = 1
            elif c == "/":
                if expression[i-1] == "0":
                    n = 10
                else:
                    n = int(expression[i-1])
                if i < len(expression) - 2 and expression[i+2] == "0":
                    d = 10
                else:
                    d = int(expression[i + 1])
                last_n = last_n*d + sign*last_d*n
                last_d = last_d*d
            i += 1
        divisor = self.gcd(abs(last_n), abs(last_d))
        return str(last_n//divisor) + "/" + str(last_d//divisor)
    
    def gcd(self, a, b):
        if b == 0:
            return a
        return self.gcd(b, a%b)