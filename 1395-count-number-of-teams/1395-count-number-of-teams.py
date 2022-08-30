class Solution(object):
    def numTeams(self, rating):
        """
        :type rating: List[int]
        :rtype: int
        """
        res = 0
        for i in range(1, len(rating) - 1):
            num = rating[i]
            leftless, leftgreat, rightless, rightgreat = 0, 0, 0, 0
            for j in range(i):
                if rating[j] > num:
                    leftgreat += 1
                else:
                    leftless += 1
            for j in range(i+1, len(rating)):
                if rating[j] > num:
                    rightgreat += 1
                else:
                    rightless += 1
            res += leftless*rightgreat + leftgreat*rightless
        return res