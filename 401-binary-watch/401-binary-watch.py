class Solution(object):
    def readBinaryWatch(self, turnedOn):
        """
        :type turnedOn: int
        :rtype: List[str]
        """
        res = []
        for h in range(12):
            for m in range(60):
                if (bin(h) + bin(m)).count("1") == turnedOn:
                    res.append("%d:%02d" % (h, m))
        return res