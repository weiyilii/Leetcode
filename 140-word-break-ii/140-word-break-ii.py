class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        res = []
        l = len(s)
        
        def dfs(i, path):
            if i == l:
                res.append(" ".join(path))
                return
            if i > l:
                return
            for word in wordDict:
                wlen = len(word)
                if i + wlen <= l and s[i:i + wlen] == word:
                    dfs(i + wlen, path + [word])
        
        dfs(0, [])
        return res