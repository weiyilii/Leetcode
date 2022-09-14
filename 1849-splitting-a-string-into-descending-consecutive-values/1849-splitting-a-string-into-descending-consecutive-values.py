class Solution:
    def splitString(self, s: str) -> bool:
        l = len(s)
        
        def dfs(start, i, prev_val):
            if i == l-1:
                return int(s[start:i+1]) == prev_val - 1
            if dfs(start, i + 1, prev_val):
                return True
            cur_val = int(s[start:i+1])
            if cur_val == prev_val - 1 and dfs(i+1, i+1, cur_val):
                return True
            return False
        
        for i in range(l - 1):
            if dfs(i+1, i+1, int(s[:i+1])):
                return True
        return False