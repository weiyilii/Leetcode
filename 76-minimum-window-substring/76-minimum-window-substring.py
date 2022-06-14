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
        char_len = len(char_counts)
        found = 0
        left, right = 0, 0
        min_len = 10**5 + 1
        res = (0, 0)
        
        while right < m:
            char = s[right]
            char_seen[char] += 1
            if char in char_counts and char_seen[char] == char_counts[char]:
                found += 1
            while left <= right and found == char_len:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    res = (left, right)
                char = s[left]
                char_seen[char] -= 1
                if char in char_counts and char_seen[char] < char_counts[char]:
                    found -= 1
                left += 1
            right += 1
        
        if min_len == 10**5 + 1:
            return ""
        else:
            return s[res[0]: res[1]+1]