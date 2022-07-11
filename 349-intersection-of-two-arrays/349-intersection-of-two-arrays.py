class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1 = list(set(nums1))
        nums2 = set(nums2)
        res = []
        for num in nums1:
            if num in nums2:
                res.append(num)
        return res