class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        l1, l2 = len(s), len(p)
        if l1 < l2:
            return []
        needs = collections.Counter(p)
        window = collections.defaultdict(int)
        valid = 0
        res = []
        left, right = 0, 0
        while right < l1:
            c = s[right]
            right += 1
            if c in needs:
                window[c] += 1
                if needs[c] == window[c]:
                    valid += 1
            while valid == len(needs):
                if right - left == l2:
                    res.append(left)
                d = s[left]
                left += 1
                if d in needs:
                    if needs[d] == window[d]:
                        valid -= 1
                    window[d] -= 1
        return res