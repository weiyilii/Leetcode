class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # DP, constant space
        if s[0] == "0":
            return 0
        
        prev1, prev2, cur = 1, 1, 1
        for i in range(1, len(s)):
            cur = 0
            num = int(s[i-1:i+1])
            if s[i] == "0":
                if num > 0 and num <= 26:
                    cur += prev1
            else:
                cur += prev2
                if num >= 10 and num <= 26:
                    cur += prev1
            prev1 = prev2
            prev2 = cur
        
        return cur
