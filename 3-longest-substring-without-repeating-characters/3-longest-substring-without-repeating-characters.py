class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        # use start and end as 2 pointers deciding max substring
        # seen as has map having letter: index pairs
        # end goes through s
        start, max_len = 0, 0
        seen = {}
        for end, letter in enumerate(s):
            # if letter has been seen and start is on the left of previously seen letter 
            # move start to the right of that seen letter
            # only in this case that mean current sub string has duplicate characters
            if letter in seen and start <= seen[letter]:
                start = seen[letter] + 1
            # No duplicate, compare max_len and length of current substring
            else:
                max_len = max(max_len, end - start + 1)
            # Add (update) key value pairs
            seen[letter] = end
        return max_len