class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        valFreq = {} # value : frequency

        for i in nums:
            valFreq[i] = valFreq.get(i, 0) + 1 
        
        a_list = []
        for val, freq in valFreq.items():
            a_list.append([freq, val])
        a_list.sort()

        res = []
        while k > len(res):
            res.append(a_list.pop()[1])
        return res