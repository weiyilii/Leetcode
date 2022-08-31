class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        arr.sort(key = lambda x: ("{0:b}".format(x).count("1"), x))
        return arr