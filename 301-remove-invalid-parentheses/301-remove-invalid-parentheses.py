class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        left, right = 0, 0
        for i in range(len(s)):
            if s[i] == "(":
                left += 1
            elif s[i] == ")":
                if left > 0:
                    left -= 1
                else:
                    right += 1
        res = set()
        l = len(s)
        
        def dfs(dell, delr, path, i):
            if i == l-1:
                if self.isValid(path) and path not in res:
                    res.add(path)
                return
            if s[i+1] == "(":
                if dell < left:
                    dfs(dell+1, delr, path, i+1)
                dfs(dell, delr, path + "(", i+1)
            elif s[i+1] == ")":
                if delr < right:
                    dfs(dell, delr+1, path, i+1)
                dfs(dell, delr, path + ")", i+1)
            else:
                dfs(dell, delr, path + s[i+1], i+1)
        
        dfs(0, 0, "", -1)
        return list(res)
    
    def isValid(self, s):
        count = 0
        for c in s:
            if c == "(":
                count += 1
            elif c == ")":
                count -= 1
                if count < 0:
                    return False
        return (count == 0)
        