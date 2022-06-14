class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        n = len(s)
        
        def dfs(start, path):
            if start == n:
                res.append(path[1:])
            for i in range(start, n):
                w = s[start:i+1]
                if w in wordDict:
                    dfs(i+1, path + " " + w)
        
        res = []
        dfs(0, "")
        return res