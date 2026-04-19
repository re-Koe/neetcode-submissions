class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        before = []
        ptr = 0
        for i in range(len(nums)):
            if i == 0:
                ptr = nums[i]
                before.append(1)
                continue
            before.append(ptr)
            ptr = ptr * nums[i]

        ptr = 1
        after = [1] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            after[i] = ptr
            ptr *= nums[i]

        final = []
        for i in range(len(before)):
            final.append(before[i] * after[i])
        
        return final
