class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def ispalindrome(s):
            return s == s[::-1]
        res = []
        dic = {word: i for i, word in enumerate(words)}
        for i in range(len(words)):
            word = words[i]
            l = len(word)
            for j in range(l+1):
                prefix = word[:j]
                suffix = word[j:]
                if ispalindrome(prefix):
                    reverse = suffix[::-1]
                    if reverse != word and reverse in dic:
                        res.append([dic[reverse], i])
                if j != l and ispalindrome(suffix):
                    reverse = prefix[::-1]
                    if reverse != word and reverse in dic:
                        res.append([i, dic[reverse]])
        return res