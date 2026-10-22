class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mappy = {} # valur : freq

        for i in nums:
            mappy[i] = mappy.get(i, 0) + 1
        

        freqVal = []
        for value, freq in mappy.items():
            freqVal.append([freq, value])
        
        freqVal.sort()
        res = []

        while len(res) < k:
            res.append(freqVal.pop()[1])
        return res