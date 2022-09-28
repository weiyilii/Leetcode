class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # res: how many left parenthes needed to be inserted
        # need: how many right parenthese needed to close left half
        res, need = 0, 0
        for c in s:
            if c == "(":
                need += 1
            else:
                need -= 1
            if need == -1:
                res += 1
                # Dont forget to reset need
                need = 0
        return res + need
