class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        res, block, s = [], False, ""
        for line in source:
            i, l = 0, len(line)
            while i < len(line):
                c = line[i]
                if c == "/" and i < l - 1 and line[i+1] == "/" and not block:
                    i = len(line)
                elif c == "/" and i < l - 1 and line[i+1] == "*" and not block:
                    i += 1
                    block = True
                elif c == "*" and i < l - 1 and line[i+1] == "/" and block:
                    i += 1
                    block = False  
                elif not block:
                    s += line[i]
                i += 1
            if s and not block:
                res.append(s)
                s = ""
        return res