class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False
        dp = [False]*(n+1)
        
        for i in range(m+1):
            for j in range(n+1):
                if i == 0 and j == 0:
                    dp[j] = True
                elif i == 0:
                    dp[j] = (s2[j-1] == s3[j-1] and dp[j-1])
                elif j == 0:
                    dp[0] = (s1[i-1] == s3[i-1] and dp[0])
                else:
                    dp[j] = (s2[j-1] == s3[i+j-1] and dp[j-1]) or (s1[i-1] == s3[i+j-1] and dp[j])
        return dp[-1]