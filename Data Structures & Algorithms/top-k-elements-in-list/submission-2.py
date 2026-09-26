class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        amap = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            amap[num] = amap.get(num, 0) + 1
        for num, count in amap.items():
            freq[count].append(num)
        
        final = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                final.append(num)
                if k == len(final):
                    return final
