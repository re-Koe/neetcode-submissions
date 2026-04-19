class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        aset = set()
        left = 0
        answer = 0

        for right in range(len(s)):
            while s[right] in aset:
                aset.remove(s[left])
                left += 1
            aset.add(s[right])
            answer = max(answer, right - left + 1)
        return answer 