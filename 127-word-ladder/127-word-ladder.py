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
        changemap = collections.defaultdict(list)
        n = len(endWord)
        for word in wordList:
            for i in range(n):
                key = word[:i] + '*' + word[i+1:]
                changemap[key].append(word)
        q = collections.deque()
        q.append((beginWord, 1))
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
                        if item not in visited:
                            visited[item] = level + 1
                            q.append((item, level + 1))
        return 0