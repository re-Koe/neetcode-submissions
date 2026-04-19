class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        amap = {}

        for i in nums:
            amap[i] = 1 + amap.get(i, 0)
        
        listy = []
        for i, j in amap.items():
            listy.append([j, i])

        listy.sort()
        final = []
        while len(final) < k:
            final.append(listy[-1-len(final)][1])
        return final