class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        from collections import deque
        visited = set()
        q = deque()
        q.append((s1, 0))
        visited.add(s1)
        while q:
            s, d = q.popleft()
            if s == s2:
                return d
            i = 0
            while i < len(s) and s[i] == s2[i]:
                i += 1
            for j in range(i, len(s)):
                if s[j] == s2[i] and s[j] != s2[j]:
                    news = s[:i] + s[j] + s[i+1:j] + s[i] + s[j+1:]
                    q.append((news, d+1))