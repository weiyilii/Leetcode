class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        
        from heapq import heappush, heappop
        
        start, end = [], []
        for b in buildings:
            l, r, h = b[0], b[1], -1*b[2]
            start.append((l, h, 's'))
            end.append((r, h, 'e'))  
       
        start = sorted(start, key=lambda tup: (tup[0], tup[1]))
        end = sorted(end, key=lambda tup: (tup[0], -tup[1]))
        
        start.extend(end)
        
        # Sort all tuples by their x-coordinate
        lines = sorted(start, key=lambda tup: tup[0])
        
        heights = [0]
        res = []
        for x, y, z in lines:
            prev_max = heights[0]
            if z == 's':
                heappush(heights, y)
                if heights[0] != prev_max:
                    res.append([x, -heights[0]])
            else:
                self.removeValueFromHeap(heights, y)
                if heights[0] != prev_max:
                    res.append([x, -heights[0]])
        return res
    
    def removeValueFromHeap(self, heap, element):
        index = None
        for i, v in enumerate(heap):
            if v ==element:
                index = i
                break
        heap[index] = heap[-1]
        heap.pop()
        heapq.heapify(heap)