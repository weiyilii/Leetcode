class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        # DP, Monotonic Queue
        from collections import deque
        n = len(nums)
        
        # score as dp, score[i] = max score can get if ends at i
        score = [0]*n
        score[0] = nums[0]
        
        # q as the decreasing queue
        q = deque([0])
        for i in range(1, n):
            # q[0] should be the largest score to add
            # But first, check if index is within range
            # popleft those elements where index < i - k
            while q and q[0] < i - k:
                q.popleft()
                
            # Now q[0] gives index, score[index] can be added to get score[i]
            score[i] = nums[i] + score[q[0]]
            
            # Keep queue decreasing, pop all elements where score[element] < score[i] 
            while q and score[q[-1]] < score[i]:
                q.pop()
            q.append(i)
        return score[-1]
        
