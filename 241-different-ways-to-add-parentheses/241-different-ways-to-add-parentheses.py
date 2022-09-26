class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        if expression.isdigit():
            return [int(expression)]
        res = []
        for i in range(len(expression)):
            if not expression[i].isdigit():
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i+1:])
                for a in left:
                    for b in right:
                        if expression[i] == "+":
                            num = a + b
                        elif expression[i] == "-":
                            num = a - b
                        elif expression[i] == "*":
                            num = a * b
                        res.append(num)
        return res