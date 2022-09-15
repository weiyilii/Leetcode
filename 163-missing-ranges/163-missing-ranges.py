class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        res = []
        for num in nums:
            if num - lower == 1:
                res.append(str(lower))
            if num - lower > 1:
                res.append(str(lower) + "->" + str(num-1))
            lower = num + 1
        if upper == lower:
            res.append(str(upper))
        if upper - lower >= 1:
            res.append(str(lower) + "->" + str(upper))
        return res