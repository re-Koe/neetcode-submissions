class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mapy = {}
        final = 0

        left = 0
        maxy = 0
        for i in range(len(s)):
            mapy[s[i]] = mapy.get(s[i], 0) + 1
            maxy = max(maxy, mapy[s[i]])

            while (i - left + 1) - maxy > k:
                mapy[s[left]] -= 1
                left += 1
            final = max(final, i - left + 1)
        
        return final