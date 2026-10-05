class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        aset = set(nums)
        longest = 0

        for i in range(len(nums)):
            length = 0
            if (nums[i] - 1) not in aset:
                length = 1
                while (nums[i] + length) in aset:
                    length += 1
                longest = max(longest, length)
        return longest