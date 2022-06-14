class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        m, n = len(s), len(t)
        if m < n:
            return ""
        
        char_counts = collections.Counter(t)
        char_seen = collections.defaultdict(int)
        # char_len is the number of unique characters in t
        char_len = len(char_counts)
        # found measures how many unique characters from t the sliding window includes
        # when char_len == found, current sliding window is desirable
        found = 0
        left, right = 0, 0
        min_len = 10**5 + 1
        res = (0, 0)
        # use right pointer to expand to right
        # when sliding window is desirable, increment left pointer to contract window
        while right < m:
            # operate one character at the right pointer each time
            char = s[right]
            char_seen[char] += 1
            if char in char_counts and char_seen[char] == char_counts[char]:
                found += 1
                
            # contract current window until it is no longer desirable
            while left <= right and found == char_len:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    res = (left, right)
                char = s[left]
                char_seen[char] -= 1
                if char in char_counts and char_seen[char] < char_counts[char]:
                    found -= 1
                left += 1
            # when current window is no longer desirable, expand using right pointer   
            right += 1
        
        if min_len == 10**5 + 1:
            return ""
        else:
            return s[res[0]: res[1]+1]