# DP with Trie
class TrieNode(object):
    def __init__(self):
        self.children = dict()
        self.is_word = False

class Trie(object):
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        cur = self.root
        for letter in word:
            if letter not in cur.children:
                cur.children[letter] = TrieNode()
            cur = cur.children[letter]
        cur.is_word = True

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        t = Trie()
        for word in wordDict:
            t.insert(word)
        l = len(s)
        dp = [False]*(l + 1)
        dp[-1] = True
        
        # Bottom up, so that each i will be the start of a word, can search in a Trie from root
        for i in range(l-1, -1, -1):
            cur = t.root
            j = i
            while j < l and cur:
                cur = cur.children.get(s[j])
                if cur and cur.is_word and dp[j+1]:
                    dp[i] = True
                    break
                j += 1
        return dp[0]
