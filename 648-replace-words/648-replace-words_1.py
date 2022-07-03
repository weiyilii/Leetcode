class TrieNode(object):
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False
        self.indx = None

class Trie(object):
    def __init__(self):
        self.root = TrieNode()
    
    def insearch(self, i, word):
        current = self.root
        for letter in word:
            current = current.children[letter]
        current.is_word = True
        current.indx = i

class Solution(object):
    def replaceWords(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: str
        """
        trie = Trie()
        for i, root in enumerate(dictionary):
            trie.insearch(i, root)
            
        words = sentence.split(" ")
        res = []
        # Be careful: root dictionary has "rf", words has "r"
        for word in words:
            new = ""
            current = trie.root
            for letter in word:
                current = current.children.get(letter)
                if current is None:
                    break
                if current.is_word:
                    new = dictionary[current.indx]
                    break
            if new == "":
                res.append(word)
            else:
                res.append(new)
        res = " ".join(res)
        return res
