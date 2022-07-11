class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dic1 = collections.Counter(nums1)
        dic2 = collections.Counter(nums2)
        res = []
        for key in dic1:
            if key in dic2:
                res += [key]*(min(dic1[key], dic2[key]))
        return res