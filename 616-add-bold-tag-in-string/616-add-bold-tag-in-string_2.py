class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        # Use an array to determine whether in bold
        op = [False]*len(s)
        for word in words:
            wl = len(word)
            index = s.find(word)
            while index != -1:
                for i in range(index, index + wl):
                    op[i] = True
                index += 1
                index = s.find(word, index)
        
        res = ""
        i = 0
        while i < len(s):
            if op[i]:
                res += "<b>"
                while i < len(s) and op[i]:
                    res += s[i]
                    i += 1
                res += "</b>"
            else:
                res += s[i]
                i += 1
        return res
