class TrieNode(object):
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False

class Trie(object):
    def __init__(self):
        self.root = TrieNode()
        self.num_of_words = 0
    
    def insert(self, word):
        current = self.root
        for letter in word:
            current = current.children[letter]
        current.is_word = True
        self.num_of_words += 1

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
        
        node = trie.root
        res = []
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                self.dfs(i, j, trie, node.children.get(board[i][j]), board, board[i][j], res)
        return res
            
    def dfs(self, i, j, trie, node, board, path, res):
        if not node or trie.num_of_words == 0:
            return
        if node.is_word:
            res.append(path)
            trie.num_of_words -= 1
            node.is_word = False
            
        tmp = board[i][j]
        board[i][j] = "#"
        
        m, n = len(board), len(board[0])
        if i+1 < m:
            c = board[i+1][j]
            self.dfs(i+1, j, trie, node.children.get(c), board, path+c, res)
        if i-1 >= 0:
            c = board[i-1][j]
            self.dfs(i-1, j, trie, node.children.get(c), board, path+c, res)
        if j+1 < n:
            c = board[i][j+1]
            self.dfs(i, j+1, trie, node.children.get(c), board, path+c, res)
        if j-1 >= 0:
            c = board[i][j-1]
            self.dfs(i, j-1, trie, node.children.get(c), board, path+c, res)
        board[i][j] = tmp
        
