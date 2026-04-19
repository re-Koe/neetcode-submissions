class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        amap = {}
        bmap = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            amap[s[i]] = 1 + amap.get(s[i], 0)
            bmap[t[i]] = 1 + bmap.get(t[i], 0)

        if amap == bmap:
            return True

        return False