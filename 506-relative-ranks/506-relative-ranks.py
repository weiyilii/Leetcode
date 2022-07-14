class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        n = len(score)
        rank = []
        for i, s in enumerate(score):
            rank.append((i, s))
        rank.sort(key = lambda x: x[1], reverse = True)
        for j in range(n):
            if j == 0:
                score[rank[j][0]] = "Gold Medal"
            elif j == 1:
                score[rank[j][0]] = "Silver Medal"
            elif j == 2:
                score[rank[j][0]] = "Bronze Medal"
            else:
                score[rank[j][0]] = str(j + 1)
        return score