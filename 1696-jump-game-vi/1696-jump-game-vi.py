class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        from collections import deque
        n = len(nums)
        score = [0]*n
        score[0] = nums[0]
        q = deque([0])
        for i in range(1, n):
            while q and q[0] < i - k:
                q.popleft()
            score[i] = nums[i] + score[q[0]]
            while q and score[q[-1]] < score[i]:
                q.pop()
            q.append(i)
        return score[-1]
        