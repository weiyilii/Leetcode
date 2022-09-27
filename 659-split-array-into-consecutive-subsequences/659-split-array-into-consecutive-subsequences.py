class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        freq = collections.Counter(nums)
        need = collections.defaultdict(int)
        for n in nums:
            if freq[n] == 0:
                continue
            else:
                if n in need and need[n] > 0:
                    freq[n] -= 1
                    need[n] -= 1
                    need[n+1] += 1
                elif n+1 in freq and n+2 in freq and freq[n+1] > 0 and freq[n+2] > 0:
                    freq[n] -= 1
                    freq[n+1] -= 1
                    freq[n+2] -= 1
                    need[n+3] += 1
                else:
                    return False
        return True