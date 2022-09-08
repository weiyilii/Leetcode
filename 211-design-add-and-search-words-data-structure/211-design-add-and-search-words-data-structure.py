class WordDictionary(object):

    def __init__(self):
        self.d = collections.defaultdict(set)

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        self.d[len(word)].add(word)

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if "." not in word:
            return word in self.d[len(word)]
        for w in self.d[len(word)]:
            match = True
            for i, c in enumerate(word):
                if c != "." and w[i] != c:
                    match = False
                    break
            if match:
                return True
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)