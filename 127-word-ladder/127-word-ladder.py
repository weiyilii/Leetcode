class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0
        # changemap records wordList's variations changing one letter
        # {*ot:["hot", "dot"], h*t:["hot"], ....}
        changemap = collections.defaultdict(list)
        n = len(endWord)
        for word in wordList:
            for i in range(n):
                key = word[:i] + '*' + word[i+1:]
                changemap[key].append(word)
        # BFS: from current word, change one letter each time 
        # and get words by mapping its root from changemap
        # these words form the new layer
        q = collections.deque()
        q.append((beginWord, 1))
        # a word might appear in new layer many times
        # Use visited to keep track of visited word
        visited = collections.defaultdict(int)
        while q:
            qlen = len(q)
            for i in range(qlen):
                word, level = q.popleft()
                if word == endWord:
                    return level
                for j in range(n):
                    key = word[:j] + '*' + word[j+1:]
                    for item in changemap[key]:
                        # Only when item is not visited, append it to visited and queue
                        if item not in visited:
                            visited[item] = level + 1
                            q.append((item, level + 1))
        return 0