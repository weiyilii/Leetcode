class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        parent = {num: num for num in nums}
        rank = {num: 1 for num in nums}
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(p, q):
            rootp = find(p)
            rootq = find(q)
            if rootp == rootq:
                return
            if rank[rootp] <= rank[rootq]:
                parent[rootp] = rootq
                rank[rootq] += rank[rootp]
            else:
                parent[rootq] = rootp
                rank[rootp] += rank[rootq]
        
        nums = set(nums)
        for num in nums:
            if num-1 in nums:
                union(num-1, num)
            if num+1 in nums:
                union(num, num+1)
        
        return max(rank.values()) if len(nums) > 0 else 0