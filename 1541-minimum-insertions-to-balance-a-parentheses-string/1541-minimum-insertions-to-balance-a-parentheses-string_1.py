class Solution:
    def minInsertions(self, s: str) -> int:
        # similar to 921
        # res records how many parenthese inserted through the process
        # need equals to the number of right half needed dynamicly
        # determine whether to insert according to insert
        
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
