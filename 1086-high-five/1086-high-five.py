class Solution(object):
    def highFive(self, items):
        """
        :type items: List[List[int]]
        :rtype: List[List[int]]
        """
        scores = collections.defaultdict(list)
        res = []
        for i, s in items:
            scores[i].append(s)
        for key in scores:
            scores[key].sort(reverse = True)
            avg = sum(scores[key][:5])//5
            res.append([key, avg])
        res.sort(key = lambda x: x[0])
        return res