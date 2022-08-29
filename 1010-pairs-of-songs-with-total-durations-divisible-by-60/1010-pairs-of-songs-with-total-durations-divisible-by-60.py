class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        count = collections.defaultdict(int)
        for t in time:
            count[t%60] += 1
        res = 0
        
        for key in count:
            if key == 0 or key == 30:
                res += count[key]*(count[key] - 1)/2
            elif (60 - key) in count:
                res += count[key]*count[60-key]
                count[60 - key] = 0
            count[key] = 0
        return res