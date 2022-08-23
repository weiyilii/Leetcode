class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        dp = [[] for _ in range(n+1)]
        dp[0] = [""]
        for i in range(n):
            for j in range(0, i+1):
                for x in dp[j]:
                    for y in dp[i-j]:
                        dp[i+1].append("(" + x + ")" + y)
        return dp[-1]