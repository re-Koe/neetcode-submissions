class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre, post = [], []
        pre_product = 1
        post_product = 1

        for i in range(len(nums)):
            if i == 0:
                pre.append(1)
                pre_product *= nums[i]
                continue
            pre.append(pre_product)
            pre_product *= nums[i]
        
        for i in range(len(nums)):
            if i == 0:
                post.append(1)
                post_product *= nums[-1]
                continue
            post.append(post_product)
            post_product *= nums[-1 - i]

        res = []
        
        for i in range(len(nums)):
            res.append(pre[i] * post[-1 - i])
        
        return res


