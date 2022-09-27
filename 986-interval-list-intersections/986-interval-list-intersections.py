class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        l1, l2 = len(firstList), len(secondList)
        p1, p2 = 0, 0
        res = []
        while p1 < l1 and p2 < l2:
            [start1, end1] = firstList[p1]
            [start2, end2] = secondList[p2]
            
            if end1 < start2:
                p1 += 1
            elif start1 > end2:
                p2 += 1
            else:
                if end1 < end2:
                    p1 += 1
                elif end1 > end2:
                    p2 += 1
                else:
                    p1 += 1
                    p2 += 1
                res.append([max(start1, start2), min(end1, end2)])
        return res
                        
                    