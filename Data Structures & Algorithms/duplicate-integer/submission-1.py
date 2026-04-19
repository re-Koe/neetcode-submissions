class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        aset = set()

        for i in nums:
            if i in aset:
                return True
            aset.add(i)

        return False