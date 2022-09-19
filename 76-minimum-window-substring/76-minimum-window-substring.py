class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)
        if m < n:
            return ""
        left, right = 0, 0
        start, l = 0, float('inf')
        needs = collections.Counter(t)
        window = collections.defaultdict(int)
        valid = 0
        while right < m:
            c = s[right]
            right += 1
            if c in needs:
                window[c] += 1
                if needs[c] == window[c]:
                    valid += 1
                
            while valid == len(needs):
                if right - left < l:
                    start = left
                    l = right - left
                d = s[left]
                left += 1
                if d in needs:
                    if window[d] == needs[d]:
                        valid -= 1
                    window[d] -= 1
        return "" if l > m else s[start:start + l]