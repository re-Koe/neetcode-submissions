class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mappy = {}
        
        listy = [[] for i in range(len(nums) + 1)]

        for i in nums:
            mappy[i] = mappy.get(i, 0) + 1
        
        for num, cnt in mappy.items():
            listy[cnt].append(num)

        res = []
        for i in range(len(listy) - 1, -1, -1):
            for num in listy[i]:
                res.append(num)
                if len(res) == k:
                    return res