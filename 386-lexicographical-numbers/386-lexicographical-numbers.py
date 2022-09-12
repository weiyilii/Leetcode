class TrieNode(object):
    def __init__(self):
        self.children = dict()
        self.is_end = False

class Solution:
    def __init__(self):
        self.root = TrieNode()
        self.res = []
    
    def insert(self, s):
        cur = self.root
        for l in s:
            if l not in cur.children:
                cur.children[l] = TrieNode()
            cur = cur.children[l]
        cur.is_end = True
    
    def printTrie(self, node, path):
        if node.is_end:
            self.res.append(int(path))
        for c in node.children:
            self.printTrie(node.children[c], path + c)

    def lexicalOrder(self, n: int) -> List[int]:
        for i in range(1, n+1):
            s = str(i)
            self.insert(s)
        self.printTrie(self.root, "")
        return self.res
        