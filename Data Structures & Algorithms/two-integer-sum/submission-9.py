class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        aset = {}

        for i in range(len(nums)):
            if target - nums[i] in aset:
                return [aset[target - nums[i]], i]
            aset[nums[i]] = i
        