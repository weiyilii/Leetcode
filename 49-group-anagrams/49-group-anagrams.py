class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # collections.defaultdict() can automatically create the key for the first time
        hashmap = collections.defaultdict(list)
        for item in strs:
            # list is a mutable object and cannot be a key
            key = tuple(sorted(item))
            hashmap[key] += [item]
        return list(hashmap.values())