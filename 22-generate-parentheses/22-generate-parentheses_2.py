class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # DP
        # dp[i] stores all results having i pairs of parentheses
        # dp[i] = [(dp[0])dp[i-1], (dp[1])dp[i-2],..., (dp[i-1])dp[0]]
        dp = [[] for _ in range(n+1)]
        dp[0] = [""]
        for i in range(n):
            for j in range(0, i+1):
                for x in dp[j]:
                    for y in dp[i-j]:
                        dp[i+1].append("(" + x + ")" + y)
        return dp[-1]
