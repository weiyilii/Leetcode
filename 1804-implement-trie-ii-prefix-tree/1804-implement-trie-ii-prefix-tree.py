class TrieNode(object):
    
    def __init__(self):
        self.children = dict()
        self.count = 0
        self.start_with = 0
    
class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        cur = self.root
        for letter in word:
            if letter not in cur.children:
                cur.children[letter] = TrieNode()
            cur = cur.children[letter]
            cur.start_with += 1
        cur.count += 1

    def countWordsEqualTo(self, word):
        """
        :type word: str
        :rtype: int
        """
        cur = self.root
        for letter in word:
            cur = cur.children.get(letter)
            if cur is None:
                return 0
        return cur.count

    def countWordsStartingWith(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        cur = self.root
        for letter in prefix:
            cur = cur.children.get(letter)
            if cur is None:
                return 0
        return cur.start_with

    def erase(self, word):
        """
        :type word: str
        :rtype: None
        """
        cur = self.root
        for letter in word:
            cur = cur.children.get(letter)
            cur.start_with -= 1
        cur.count -= 1

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)