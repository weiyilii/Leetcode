class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # res: how many parenthes should be inserted through the scanning process
        # need records how many right half needed through the process 
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
        # at last may still need some right halves. should insert them so return res + need.
        return res + need
