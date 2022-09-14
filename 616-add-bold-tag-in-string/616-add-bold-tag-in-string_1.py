class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        # Merge Intervals
        intervals = []
        for word in words:
            wl = len(word)
            index = s.find(word)
            while index != -1:
                intervals.append([index, index + wl])
                # Update index by 1 and find next word: s = "zzz", word = "zz"
                index += 1
                index = s.find(word, index)
        if len(intervals) == 0:
            return s
        intervals.sort(key = lambda x: (x[0], x[1]))
        merge = [intervals[0]]
        for i in range(1, len(intervals)):
            if merge[-1][1] >= intervals[i][0]:
                merge[-1][1] = max(merge[-1][1], intervals[i][1])
            else:
                merge.append(intervals[i])

        res = ""
        prev = 0
        for start, end in merge:
            res += s[prev:start]
            res += "<b>"
            res += s[start:end]
            res += "</b>"
            prev = end
        if prev < len(s):
            res += s[prev:]
        
        return res
