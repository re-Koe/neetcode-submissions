class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        amap = {} # value, index
        for i in range(len(nums)):
            if (target - nums[i]) in amap.keys():
                return [amap[target - nums[i]], i]
            amap[nums[i]] = i