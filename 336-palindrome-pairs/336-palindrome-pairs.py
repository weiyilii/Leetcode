class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        def ispalindrome(s):
            return s == s[::-1]
        res = []
        dic = {word: i for i, word in enumerate(words)}
        for i in range(len(words)):
            word = words[i]
            n = len(word)
            # for a word "bot", pref = "", "b", "bo", "bot"
            # if pref is palindrome ("", "b") (their surf: "bot", "ot")
            # check if reversed surf in words ("tob", "to")
            # if any in, reversed surf + word is a palindrome
            for j in range(n+1):
                pref = word[:j]
                surf = word[j:]
                if ispalindrome(pref):
                    reverse = surf[::-1]
                    if reverse != word and reverse in dic:
                        res.append([dic[reverse], i])
                if j != n and ispalindrome(surf):
                    reverse = pref[::-1]
                    if reverse != word and reverse in dic:
                        res.append([i, dic[reverse]])
        return res