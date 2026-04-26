class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seenVal = set()
        for i in nums:
            if i in seenVal:
                return i
            seenVal.add(i)
        