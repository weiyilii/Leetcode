class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        # Heap
        from heapq import heappop, heappush
        res = []
        visited = {(0, 0)}
        # maintain a heap h whose h[0] = (s,(n1, n2)) always has samllest s (nums1[n1]+nums2[n2])
        h = [(nums1[0]+nums2[0], (0, 0))]
        l1, l2 = len(nums1), len(nums2)
        while len(res) < k and h:
            n1, n2 = heappop(h)[1]
            res.append([nums1[n1], nums2[n2]])
            # n1, n2 are both ascending
            # smallest sum must be nums1[0]+nums2[0]
            # next smallest sum can only be given by (n1+1, n2) or (n1, n2+1)
            new_n1 = n1+1 if n1 < l1-1 else n1
            new_n2 = n2+1 if n2 < l2-1 else n2
            if (new_n1, n2) not in visited:
                s = nums1[new_n1] + nums2[n2]
                heappush(h, (s, (new_n1, n2)))
                visited.add((new_n1, n2))
            if (n1, new_n2) not in visited:
                s = nums1[n1] + nums2[new_n2]
                heappush(h, (s, (n1, new_n2)))
                visited.add((n1, new_n2))
        return res
