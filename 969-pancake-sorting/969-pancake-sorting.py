class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        self.res = []
        self.psort(arr, len(arr))
        return self.res
        
    def psort(self, arr, n):
        if n == 1:
            return
        maxCake = 0
        for i in range(1, n):
            if arr[maxCake] < arr[i]:
                maxCake = i
        if maxCake != n-1:
            self.res.append(maxCake + 1)
            self.reverse(arr, maxCake)
            self.res.append(n)
            self.reverse(arr, n-1)
        self.psort(arr, n-1)
    
    def reverse(self, arr, pos):
        i, j = 0, pos
        while i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1