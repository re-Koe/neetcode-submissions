class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        final = [1] * len(nums) # [1, 1, 1, 1]
        prefix = 1
        for i in range(len(nums)):
            final[i] = prefix
            prefix = prefix * nums[i]

        postfix = 1
        for i in range(len(nums) - 1, 0 - 1, -1):
            final[i] = final[i] * postfix
            postfix = postfix * nums[i]
        
        return final

        # [1, 2, 4, 6]
        # [1, 1, 2, 8]
        # [48, 24, 6, 1]
        # [1, 6, 24, 48]