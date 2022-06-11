class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Use a dictionary as hash map
        hashmap = {}
        # iterate through nums
        # for every index value pair, key = target - value
        # if value not in hashmap, create new pairs, key: index
        # if value == a key, that means that key has a value that sum to target
        # return that key's value (index 1) and current index (index 2)
        for index, value in enumerate(nums):
            key = target - value
            if value in hashmap:
                return [hashmap[value], index]
            else:
                hashmap[key] = index