class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort(reverse = True)
        h = 0
        for i in range(len(citations)):
            if citations[i] >= (i+1):
                h += 1
        return h