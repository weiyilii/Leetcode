class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # DP, without extra space, logic is simpler
        if s[0] == "0":
            return 0
        
        prev1, prev2, cur = 1, 1, 1
        for i in range(1, len(s)):
            cur = 0
            num1 = int(s[i])
            num2 = int(s[i-1:i+1])
            if num1 > 0:
                cur += prev2
            if num2 >= 10 and num2 <= 26:
                cur += prev1
            prev1 = prev2
            prev2 = cur
        
        return cur
