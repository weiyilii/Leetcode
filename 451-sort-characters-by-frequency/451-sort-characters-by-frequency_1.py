class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Bucket sort
        count = collections.Counter(s)
        freq = count.values()
        high, low = max(freq), min(freq)
        buckets = [[] for i in range(high - low + 1)]
        res = ''
        
        for letter in count:
            n = count[letter]
            buckets[high - n] += [letter*n]
            
        for bucket in buckets:
            res += ''.join(bucket)
        return res
