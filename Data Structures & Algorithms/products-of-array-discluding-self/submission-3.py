class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # product of all numbers before the index 
        preList = []
        preProduct = 1
        
        for i in range(len(nums)):
            if i == 0:
                preList.append(1)
                preProduct *= nums[i]
                continue
            preList.append(preProduct)
            preProduct *= nums[i]

        # product of all numbers after the index

        postList = []
        postProduct = 1

        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                postList.append(1)
                postProduct *= nums[i]
                continue
            postList.append(postProduct)
            postProduct *= nums[i]
        
        res = []

        for i in range(len(nums)):
            res.append(preList[i] * postList[-1 - i])

        return res