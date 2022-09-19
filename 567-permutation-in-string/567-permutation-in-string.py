class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1, l2 = len(s1), len(s2)
        if l1 > l2:
            return False
        needs = collections.Counter(s1)
        window = collections.defaultdict(int)
        valid = 0
        left, right = 0, 0
        while right < l2:
            c = s2[right]
            right += 1
            if c in s1:
                window[c] += 1
                if needs[c] == window[c]:
                    valid += 1
            while valid == len(needs):
                if right - left == l1:
                    return True
                d = s2[left]
                left += 1
                if d in s1:
                    if window[d] == needs[d]:
                        valid -= 1
                    window[d] -= 1
        return False    