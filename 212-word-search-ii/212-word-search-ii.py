class TrieNode(object):
    def __init__(self):
        self.children = dict()
        self.word = None

class Trie(object):
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        cur = self.root
        for letter in word:
            if letter not in cur.children:
                cur.children[letter] = TrieNode()
            cur = cur.children[letter]  
        cur.word = word

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        res = []
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                self.dfs(i, j, trie.root, board, res)
        return res
            
    def dfs(self, i, j, node, board, res):
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] not in node.children:
            return
        
        cell = board[i][j]
        next_node = node.children[cell]
        if next_node.word != None:
            res.append(next_node.word)
            next_node.word = None
            if not next_node.children.keys():
                del node.children[cell]
                return
            
        board[i][j] = "#"
        
        for x, y in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            self.dfs(i + x, j + y, next_node, board, res)
        
        board[i][j] = cell