class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        envelopes.sort(key = lambda x: (x[0], -x[1]))
        n = len(envelopes)
        
        size = 0
        tail = []
        
        for (w, h) in envelopes:
            if not tail or h > tail[-1]:
                tail.append(h)
                size += 1
            else:
                l, r = 0, size
                while l < r:
                    m = l + (r - l) // 2
                    if tail[m] < h:
                        l = m + 1
                    else:
                        r = m
                tail[l] = h
            
        return size