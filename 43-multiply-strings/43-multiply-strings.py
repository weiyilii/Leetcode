class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        l1, l2 = len(num1), len(num2)
        res = [0]*(l1 + l2)
        i, j = 0, 0
        for i in range(l1-1, -1, -1):
            for j in range(l2-1, -1, -1):
                p = int(num1[i])*int(num2[j])
                mul = p + res[i+j+1]
                res[i+j+1] = mul%10
                res[i+j] += mul//10
        i = 0
        while i < l1 + l2 and res[i] == 0:
            i += 1
        ans = ""
        for j in range(i, l1+l2):
            ans += str(res[j])
        return ans if ans else "0"