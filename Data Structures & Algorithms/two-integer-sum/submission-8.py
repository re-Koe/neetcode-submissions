class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ind_map = {} # value : index

        for i in range(len(nums)):
            if target - nums[i] in ind_map:
                return [ind_map[target - nums[i]], i]
            ind_map[nums[i]] = i
        