class Solution:
    def plusOne(self, s, i):
        if s[i] == "9":
            c = "0"
        else:
            c = str(int(s[i]) + 1)
        return s[:i] + c + s[i+1:]
    
    def minusOne(self, s, i):
        if s[i] == "0":
            c = "9"
        else:
            c = str(int(s[i]) - 1)
        return s[:i] + c + s[i+1:]
    
    def openLock(self, deadends: List[str], target: str) -> int:
        from collections import deque
        visited = set(deadends)
        q = deque()
        if "0000" not in visited:
            q.append("0000")
            visited.add("0000")
        step = 0
        while q:
            l = len(q)
            for _ in range(l):
                cur = q.popleft()
                if cur == target:
                    return step
                
                for i in range(4):
                    new = self.plusOne(cur, i)
                    if new not in visited:
                        q.append(new)
                        visited.add(new)
                    new = self.minusOne(cur, i)
                    if new not in visited:
                        q.append(new)
                        visited.add(new)
            step += 1
        return -1