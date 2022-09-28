class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        res, need = 0, 0
        for c in s:
            if c == "(":
                need += 1
            else:
                need -= 1
            if need == -1:
                res += 1
                need = 0
        return res + need