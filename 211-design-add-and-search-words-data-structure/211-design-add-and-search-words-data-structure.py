class TrieNode(object):
    
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False

class WordDictionary(object):

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        current = self.root
        for letter in word:
            current = current.children[letter]
        current.is_word = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        def dfs(current, word):
            if not word:
                if current.is_word:
                    self.res = True
                    return
            else:
                if word[0] == ".":
                    for node in current.children.values():
                        dfs(node, word[1:])
                else:
                    current = current.children.get(word[0])
                    if current is None:
                        return
                    else:
                        dfs(current, word[1:])
        
        self.res = False
        current = self.root
        dfs(current, word)
        return self.res


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)