class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_map = {} # r:2, ..., c:2
        t_map = {}

        for char in range(len(s)):
            s_map[s[char]] = s_map.get(s[char], 0) + 1
            t_map[t[char]] = t_map.get(t[char], 0) + 1
        
        return s_map == t_map
        
