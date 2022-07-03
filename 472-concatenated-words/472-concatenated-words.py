class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        d = set(words)
        memo = {}
        def dfs(word):
            if word in memo:
                return memo[word]
            memo[word] = False
            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]
                if prefix in d and suffix in d:
                    memo[word] = True
                    break
                if prefix in d and dfs(suffix):
                    memo[word] = True
                    break
                if suffix in d and dfs(prefix):
                    memo[word] = True
                    break
            return memo[word]
        res = [word for word in words if dfs(word)]
        return res