class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l = len(nums1) + len(nums2)
        if l % 2 == 1:
            return self.kth(nums1, nums2, l//2)
        else:
            return float(self.kth(nums1, nums2, l//2) + self.kth(nums1, nums2, l//2-1))/2
        
    def kth(self, nums1, nums2, k):
        if not nums1:
            return nums2[k]
        if not nums2:
            return nums1[k]
        
        i1, i2 = len(nums1)//2, len(nums2)//2
        n1, n2 = nums1[i1], nums2[i2]
        
        if i1 + i2 < k:
            if n1 < n2:
                return self.kth(nums1[i1+1:], nums2, k - i1 - 1)
            else:
                return self.kth(nums1, nums2[i2+1:], k - i2 - 1)
        else:
            if n1 < n2:
                return self.kth(nums1, nums2[:i2], k)
            else:
                return self.kth(nums1[:i1], nums2, k)