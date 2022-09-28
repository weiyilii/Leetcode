class Solution:
    def minInsertions(self, s: str) -> int:
        res, need = 0, 0
        for c in s:
            if c == "(":
                need += 2
                if need % 2 == 1:
                    res += 1
                    need -= 1
            else:
                need -= 1
                if need == -1:
                    res += 1
                    need = 1
        return res + need