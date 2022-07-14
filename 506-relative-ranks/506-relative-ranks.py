class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        n = len(score)
        res = [[] for _ in range(n)]
        rank = []
        for i, s in enumerate(score):
            rank.append((i, s))
        rank.sort(key = lambda x: x[1], reverse = True)
        for j in range(n):
            if j == 0:
                res[rank[j][0]] = "Gold Medal"
            elif j == 1:
                res[rank[j][0]] = "Silver Medal"
            elif j == 2:
                res[rank[j][0]] = "Bronze Medal"
            else:
                res[rank[j][0]] = str(j + 1)
        return res